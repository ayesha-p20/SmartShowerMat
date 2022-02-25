# importing twilio
from twilio.rest import Client
from database import *
  
# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'ACb439647b67b85890971656d4093b8c1e'
auth_token = '315edd4d98e56f25ba97f9c94ccd8e21'
  
client = Client(account_sid, auth_token)

#obtaining user's name from the database
user = userName()
messBody = "Smart Shower Mat: Your contact {0} has had a fall".format(user)

#obtaining emergency contact's ph
ephone = emergencyPhone() #make sure it's strong

''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
                              from_='+17655713379',
                              body = messBody,  
                              to ='+18588323928'
                          )
  
print(message.sid)
