import pyrebase

config = {
    'apiKey': "AIzaSyBgVgPVRtoDxAREZRbWVfxQ_mMFC6kxLMA",
    'authDomain': "fyp-breastcancer.firebaseapp.com",
    'projectId': "fyp-breastcancer",
    'storageBucket': "fyp-breastcancer.appspot.com",
    'messagingSenderId': "654106889184",
    'appId': "1:654106889184:web:ee8f3bce3e08393938b985",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)
auth.send_email_verification(user['idToken'])

