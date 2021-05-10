
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


# load in models and structures

# encodings categories
filename = r'.\saved\rfPipeLine.sav'
rfPipe = pickle.load(open(filename, 'rb'))

#load data
banking_df = pd.read_csv(".\\csvs\\cibcMar_Apr21.csv",names = ["date","name","credit","debt","account"])
banking_df = banking_df.fillna(0)
banking_df = banking_df.drop(['account'], axis=1)

credit_df = banking_df[banking_df["credit"] == 0]
debt_df = banking_df[banking_df["debt"] == 0]

df.category = df.category.replace(to_replace ='#\w*\d+', value = '', regex = True)
debt_df['name'] = debt_df['name'].replace(to_replace =',\s*[A-Z][A-Z]', value = '', regex = True)
debt_df.name = debt_df.name.replace(to_replace ='#\w*\d+', value = '', regex = True)


print(banking_df)
print()


# predict
results = rfPipe.predict(debt_df['name'])

# convert back
resultsCategories = en.inverse_transform(result)
print(resultsCategories)

debt_df['cat_id'] = results
debt_df['cat'] = resultsCategories

#save
debt_df['cat_id'] = res
debt_df['cat'] = resultsCategories

#display wanted metrics like top cost in each category

# sum each category
# sub totals for the same expense ie mcD
# largest

#graph spending bar and circle
