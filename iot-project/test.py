import pandas as pd
import firebase_admin
from firebase_admin import credentials,firestore
import time

cred=credentials.Certificate("C:/Users/Tripti/OneDrive/Desktop/iot training'/iot-project/iot-bvp-firebase.json" )
firebase_admin.initialize_app(cred,{'databaseURL':'https://iot-bvp.firebaseio.com/'})
db=firestore.client()
doc_ref=db.collection('data')
df=pd.read_csv("C:/Users/Tripti/OneDrive/Desktop/iot training'/iot-project/Occupancy.csv")
tmp=df.to_dict(orient='records')
for rec in tmp:
    print(rec)
    doc_ref.add(rec)
    print('added entry')
    time.sleep(30)