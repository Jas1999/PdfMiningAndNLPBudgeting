
import os
from collections import Counter
from flask import Flask, render_template, request, redirect, url_for

from csvAccounting import csvCatandAccount
 
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)

        PredictAndAppend(uploaded_file.filename)

    return redirect(url_for('index'))

def PredictAndAppend(fileName):

    encoderPath = r'.\saved\categoryEncoder.sav'
    modelPath = r'.\saved\rfPipeLine.sav'

    analysis =  csvCatandAccount(encoderPath, modelPath, fileName)
 
    banking_df =  analysis.predict()
    
    banking_df.to_csv("banking_df.csv", mode='a', header=True)

    banking_df['name'] = banking_df['name'].replace(to_replace =',\s*[A-Z][A-Z]', value = '', regex = True)
    banking_df.name = banking_df.name.replace(to_replace ='#\w*\d+', value = '', regex = True)

    #add cat
    credit_df = banking_df[banking_df["credit"] == 0]
    debt_df = banking_df[banking_df["debt"] == 0]
 
    print('done ')
    print(banking_df)
    # sum each category
    debtDisplaySum = debt_df.groupby('cat').sum()
    print(debtDisplaySum)
    debtDisplaySum.to_csv("banking_df.csv", mode='a', header=True)

    print('top 3 cat')
    # show top 3 in each cateogry
    for key,i in debt_df.groupby('cat'):
        print(key)
        print("sum: " + str(i['credit'].sum()))
        
        nameCat = i.groupby("name")['credit'].sum().nlargest(3) #.sum().max()
        print( (nameCat) )
if __name__ == '__main__':
    app.run(debug=True)