
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
    banking_df.to_csv("banking_df.csv", mode='a', header=False)
    
    print('done ')
    print(banking_df)

if __name__ == '__main__':
    app.run(debug=True)