import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('smartshowermat-firebase-adminsdk-m7ead-b380c34a0e.json')
firebase_admin.initialize_app(cred,{
        'databaseURL': 'https://smartshowermat-default-rtdb.firebaseio.com/'
    })

ref = db.reference('/')

ref.set({
    'SensorData':{
            'r1':{
                'ADC': 6000,
                'Raw': 0.2,
                'ADCIndex': 1,  #which adc read the value
                'Channel': 5    #which channel of adc
            },
            'r2':{
                'ADC': 56000,
                'Raw': 2.5,
                'ADCIndex': 3,  #which adc read the value
                'Channel': 2    #which channel of adc
            }
        }
    })

#adding data using push
ref2 = db.reference('Biometric')

bio_ref = ref2.push({
    'age': 66,
    'weight': 171.5, #in lb
    'pressure': 0.1,
    'activeSensors': 10,
})

#key = bio_ref.key

#reading data
print(bio_ref.get())

#deleting data
bio_ref.delete()




'''
#updating one child

ref2 = db.reference('SensorData')
r1_ref = ref2.child('r1')

r1_ref.update({
    'ADC': 5500
})
'''
'''
#updating multiple children
ref3 = db.reference('SensorData')
ref3.update({
    'r1/Raw':0.12,
    'r2/Channel': 3
})

'''










































