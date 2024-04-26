from flask import Flask, redirect, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
import hashlib
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db.init_app(app)

cred = credentials.Certificate("Creds_python.json")

database_url = {
    'databaseURL': 'https://randomizer-3a096-default-rtdb.europe-west1.firebasedatabase.app'
}

firebase_admin.initialize_app(cred, database_url)

db =  firestore.client()



@app.route('/')
def index():
    return render_template('login_register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    surname = request.form['Surname']
    password = request.form['password']

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user_data = {
        'name': name,
        'surname': surname,
        'password': hashed_password
    }
    db.collection('users').add(user_data)

    return render_template('login_register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    users_ref = db.collection('users')
    query = users_ref.where('name', '==', username).limit(1)
    user_data = query.get()

    print("User data:", user_data) 

    if user_data:
        user_doc = user_data[0].to_dict()

        print("User document:", user_doc)  

        if hashlib.sha256(password.encode()).hexdigest() == user_doc['password']:
            print("Login successful!")  # Print success message for debugging
            return render_template('index.html')
        else:
            error_message = "Incorrect password. Please try again."
            print("Incorrect password.")  # Print error message for debugging
            return render_template('login_register.html', error_message=error_message)
    else:
        error_message = "User not found. Please register first."
        print("User not found.")  # Print error message for debugging
        return render_template('login_register.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
