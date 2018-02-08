import requests
import time

url = 'https://us-central1-sleipnir-metro.cloudfunctions.net/api/trip/'
query = {
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

res = requests.post(url, data=query)
print(res.text)
