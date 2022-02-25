#Code for storing & retrieving data to and from firebase db

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('smartshowermat-firebase-adminsdk-m7ead-b380c34a0e.json')
firebase_admin.initialize_app(cred,{
        'databaseURL': 'https://smartshowermat-default-rtdb.firebaseio.com/'
        })
sensor_ref = db.reference('SensorData')
biometric_ref = db.reference('Biometrics')
user_ref = db.reference('Contact')
    

#function to write pressure sensor data to db
def writePressure(data):
    sensorInstance = sensor_ref.push(data)
    print('New object added to SENSOR DATA:',data)
    return sensorInstance

#function to read pressure sensor data from db
def readPressure(sensorInstance):
    sensorData = sensorInstance.get()
    print("Retrieved data from SENSOR DATA:",sensorData)
    return sensorData

#function to write user's biometric data to db
def writeBiometrics(bio):
    bioInstance =  biometric_ref.push(bio)
    print('New object added to BIOMETRICS:',bio)
    return bioInstance

#function to red user's biometric data from db
def readBiometrics(bioInstance):
    bioData = bioInstance.get()
    print("Retrieved data from BIOMETRICS:",bioData)
    return bioData

#function to retrieve emergency contact's phone number
def emergencyPhone():
    snapshot = user_ref.order_by_child('eContactPhone').get()
    for key, val in snapshot.items():
        print('key:{0}'.format(val['eContactPhone']))

#function to write user's contact info to db

def writeUser(user):
    userInstance = user_ref.push(user)
    print('New object added to CONTACT:',user)
    return userInstance

#function to read user's contact info from db
def readUser(userInstance):
    userData = userInstance.get()
    print("Retrieved data from CONTACT:",userData)
    return userData

#function to delete a child entry
def deleteChild():
    pass


