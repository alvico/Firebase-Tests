import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import firestore

data = {
    u'driverid': u'some_driver_id',
    u'carid': u'some_car_id',
    u'origin': {
        u'point': u'11.00, 11.00',
        u'address': u'some address',
        u'departure': time.time(),
    },
    u'destination': {
        u'point': u"22.00, 22.00",
        u'address': u'some street and number',
        u'arrival': time.time(),
    },
    u'route': u'someroute',
    u'meeting': [
        {u'mp': {
            u'location': u"33.0, 44.0",
            u'time': time.time(),
            u'passengers': []
        }},
    ],
    u'seats': 3,
    u'passengers': 3,
    u'type': u'from work',
    u'kms': 44,
    u'cost': 13,
    u'createdAt': time.time()
}

# Use a service account
cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
try:
    db.collection(u'Open').document(u'testtrip1')
except Exception as ex:
    pass
doc_ref = db.collection(u'Open').document(u'testtrip1')

doc_ref.set(data)

time.sleep(5)

doc_ref.update({u'seats': 0})
