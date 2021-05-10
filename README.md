# PdfMiningAndBudgeting
Project has a pdf mining script that creates a csv that was used to predict expenditure categories

For the project to use regex on pdfs (the current code is ones from my bank so some modifications might be necessary)

Used jupyter notebook to get the data and for training the model and testing:
start juptyer notebook with:
    jupyter notebook

get the data from pdfs with: getBudgetData.ipynb

Train models with: nlpBudget-Clean.ipynb
    -> model trained and used was at the end called rfPipeline that has the tfidf transformer saved
    -> 91% accuracy and high f1 scores for most categories (need more data to better balance, all of it is restaurants :) )

The model can be ran and used to get summations and graphs with : csvAccounting.py and nlpPickleTest.ipynb


*note I gave a example csv, but no pdfs since that has banking information

Resources used:

pdf:
https://www.tutorialspoint.com/python/python_reg_expressions.htm
https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

nlp classifications: tutorials were completed to get code working

https://towardsdatascience.com/https-medium-com-vishalmorde-humanizing-customer-complaints-using-nlp-algorithms-64a820cef373
https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
https://monkeylearn.com/text-classification/
