import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate("lc-sandbox-c942a-firebase-adminsdk-mkl9j-532701bce3.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://lc-sandbox-c942a-default-rtdb.europe-west1.firebasedatabase.app/'})
 
ref = db.reference('/') # Reference to root node of database
 
sleepData = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv', keep_default_na=False) # reads the file (dataframe)
# 'keep_default_na=False' means that when a value is 'None' it keeps it as 'None'

# Removing and replacing unnecessary data
sleepData = sleepData.replace('Normal Weight', 'Normal')
sleepData = sleepData.drop(columns = 'Person ID')
sleepData = sleepData.drop(columns = 'Blood Pressure')

# Saves cleaned data as a csv file WITHOUT the numbers in index
sleepData.to_csv('Cleaned.csv', index=False)
 
# Saves data as a dict by rows where each person is own dictionary
dataDict = sleepData.to_dict(orient='index')
 
# Uploads info to database
ref.set(dataDict)