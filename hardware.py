from database import *

#create new user
user = {
    'fname': 'Peter',
    'lname': 'Anteater',
    'phone': 9491234567,
    'email': 'peterant@uci.edu',
    'eContactName': 'Alice Anteater',
    'eContactPhone': 9497654321,
    'eContactEmail': 'alice_anteater@uci.edu'
    }

tup = writeUser(user)
#print("Key: ",tup[1])
print(type(tup))
print("lname:", tup['lname'])
