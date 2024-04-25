from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("Creds_python.json")

database_url = {
    'databaseURL': 'https://randomizer-3a096-default-rtdb.europe-west1.firebasedatabase.app'
}

firebase_admin.initialize_app(cred, database_url)

ref = db.reference('/')



@app.route('/')
def index():
    return render_template('login_register.html')

@app.route('/register', methods=['POST'])
def register():
    # Get registration data from the request
    registration_data = request.json
    print(registration_data)

    # Make a POST request to send the registration data to Firebase
    response = requests.post(database_url + 'registrations.json', json=registration_data)

    # Check if the request was successful
    if response.ok:
        return 'Registration successful'
    else:
        return 'Failed to register: ' + response.text, 500

if __name__ == '__main__':
    app.run(debug=True)
