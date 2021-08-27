
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
# load in models and structures
filename = r'.\saved\categoryEncoder.sav'
en = pickle.load(open(filename, 'rb'))

# encodings categories
filename = r'.\saved\rfPipeLine.sav'
rfPipe = pickle.load(open(filename, 'rb'))



#load data
banking_df = pd.read_csv(".\\csvs\\bankingInfo.csv",names = ["date","name","credit","debt","account"])
banking_df = banking_df.fillna(0)
banking_df = banking_df.drop(['account'], axis=1)

credit_df = banking_df[banking_df["credit"] == 0]
debt_df = banking_df[banking_df["debt"] == 0]

#df.category = df.category.replace(to_replace ='#\w*\d+', value = '', regex = True)
debt_df['name'] = debt_df['name'].replace(to_replace =',\s*[A-Z][A-Z]', value = '', regex = True)
debt_df.name = debt_df.name.replace(to_replace ='#\w*\d+', value = '', regex = True)

credit_df['cat'] = "payment"
credit_df['cat_id'] = 100 # add to encoding later 

print(banking_df)
print()


# predict
results = rfPipe.predict(debt_df['name'])

# convert back
resultsCategories = en.inverse_transform(results)
print(resultsCategories)
#save
debt_df['cat_id'] = results
debt_df['cat'] = resultsCategories
#debt_df['cat_id'] = res
#debt_df['cat'] = resultsCategories

#display wanted metrics like top cost in each category

# sum each category
debtDisplaySum = debt_df.groupby('cat').sum()
print(debtDisplaySum)
# sub totals for the same expense ie mcD
Comp_df = pd.concat([debt_df,credit_df])

BankingCategories = Comp_df.drop(['cat_id'], axis=1).groupby(["cat"]).sum()
BankingCategories = BankingCategories.reset_index()
print(BankingCategories)
print()
# largest
# show top 3 in each cateogry
for key,i in debt_df.groupby('cat'):
    print(key)
    print("sum: " + str(i['credit'].sum()))
    
    nameCat = i.groupby("name")['credit'].sum().nlargest(3) #.sum().max()
    print( (nameCat) )

#graph spending bar and circle
plt.pie(BankingCategories["credit"], labels =  BankingCategories["cat"],autopct='%2.5f%%',startangle=90)
plt.axis('equal')
plt.show()

plt.bar(BankingCategories["cat"],BankingCategories["credit"] )
plt.show()