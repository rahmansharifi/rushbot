import firebase_admin
from firebase_admin import credentials, db, storage
import random

import time

firebase_admin.initialize_app(
    credentials.Certificate('rush.json'),
    {
        'databaseURL':'https://rush-93940-default-rtdb.firebaseio.com/',
        # 'storageBucket':'store-9ed7d.appspot.com'
    }
)

class firebase:
    def __init__(self, path):
        self.path = '/'+path
    def reference(self, path):
        return db.reference(self.path+'/'+path)
    def random(self, l=16):
        out = ''
        for i in range(l):
            out += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-_')
        return out
    def load(self):
        return self.reference('').get()
    def read(self, path):
        return self.reference(path).get()
    def push(self, content):
        return self.reference('').push(content).key
    def update(self, path, content):
        return self.reference('').child(path[1::] if path.startswith('/') else path).update(content)
    def delete(self, path):
        return self.reference('').child(path[1::] if path.startswith('/') else path).set({})

class firestore:
    def upload(f):
        storage = firebase_admin.storage.bucket()
        out = ''
        for i in range(32):
            out += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')
        blob = storage.blob(out+'.jpg')
        blob.upload_from_filename(f)
        blob.make_public()
        return blob.public_url