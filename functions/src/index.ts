import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';
import * as express from 'express';
// // Start writing Firebase Functions
// // https://firebase.google.com/functions/write-firebase-functions
//
const app = express();
//export const helloWorld = functions.https.onRequest((request, response) => {
//    response.send("Hello Metro-lab");
//    console.log('helloWorld function triggered')
//});

admin.initializeApp({
    credential: admin.credential.applicationDefault()
});

app.post('/trip', (req, res) => {
    const trip = req.body;
    console.log('trip received');
    const db = admin.firestore();
    const setDoc = db.collection('Open').doc('testtrip').set(trip);
    res.send('testtrip created');
});

exports.api = functions.https.onRequest(app);

export const watchUpdates = functions.firestore.document('Open/{tripId}').onUpdate(event => {
    const newValue = event.data.data();
    if(newValue.seats === 0) {
        console.log("trip "+ event.params.tripId);
        return event.data.ref.delete();
    } else {
        return;
    }
});

export const watchDeletes = functions.firestore.document('Open/{tripId}').onDelete( event => {
    const deletedValue = event.data.previous.data();
    const tripId = event.params.tripId;
    console.log("Deleted value " + tripId);
    if(deletedValue.seats === 0) {
        console.log("trip "+ tripId + " deleted");
        const db = admin.firestore();
        const setDoc = db.collection('Closed').doc(tripId).set(deletedValue);
        return setDoc.then( res => { console.log('Set: ', res); });
    } else { 
        return Promise.resolve('Nothing to do'); 
    }
});
