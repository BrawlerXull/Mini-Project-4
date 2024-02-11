import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyC7ugvSIreXDECEVh-nX49qRHpem_TsiLY",
  "authDomain": "organizer-chinmay.firebaseapp.com",
  "databaseURL": "https://organizer-chinmay-default-rtdb.firebaseio.com",
  "projectId": "organizer-chinmay",
  "storageBucket": "organizer-chinmay.appspot.com",
  "messagingSenderId": "1028259423353",
  "appId": "1:1028259423353:web:7fd993fa6f30f3df6ea0a8",
  "measurementId": "G-PVGVGZMBYK"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

email = 'user1@example.com'
password = 'secretPassword'

# Create a new user
user_info = auth.create_user_with_email_and_password(email, password)

print('Successfully created new user:')
print(f"Local ID: {user_info['localId']}")
print(f"Email: {user_info['email']}")
