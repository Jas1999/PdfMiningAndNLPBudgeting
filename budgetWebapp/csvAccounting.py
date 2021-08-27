
# libariries for RF model
import pandas as pd
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import pickle



class csvCatandAccount():
    
    def __init__(self, encoderPath, modelPath, fileName):
        # load in encodings and structures
        self.en = pickle.load(open(encoderPath, 'rb'))
        # model
        self.rfPipe = pickle.load(open(modelPath, 'rb'))

        self.fileName = fileName

    def getData(self):
        banking_df = pd.read_csv(self.fileName)
        #clean file 
        banking_df = banking_df.fillna(0)
        banking_df = banking_df.drop(['account'], axis=1)

        return banking_df
        
    def predict(self):

        #self.banking_df = getData()
        # add columns and read 
        banking_df = pd.read_csv(self.fileName,names = ["date","name","credit","debt","account"])
        #clean file 
        banking_df = banking_df.fillna(0)
        banking_df = banking_df.drop(['account'], axis=1)

        debt_df = banking_df[banking_df["debt"] == 0]
        #df.category = df.category.replace(to_replace ='#\w*\d+', value = '', regex = True)
        debt_df ['name'] = debt_df ['name'].replace(to_replace =',\s*[A-Z][A-Z]', value = '', regex = True)
        debt_df .name = debt_df .name.replace(to_replace ='#\w*\d+', value = '', regex = True)
        
        credit_df = banking_df[banking_df["credit"] == 0]
        credit_df['cat'] = "payment"
        #credit_df['cat_id'] = -100 # add to encoding later 
        
        # predict
        results = self.rfPipe.predict(debt_df['name'])

        # convert back
        resultsCategories = self.en.inverse_transform(results)
        print(resultsCategories)
        #save
        #debt_df['cat_id'] = results
        debt_df['cat'] = resultsCategories

        return pd.concat([debt_df,credit_df])


