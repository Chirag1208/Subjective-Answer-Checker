import pyrebase
from flask import Flask
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import render_template, request, redirect, session
#from app import app
import os

config = {
    "apiKey": "AIzaSyCB4O0-4IkIK_G9HDid-0IJaayGs1S5dXU",
    "authDomain": "subjective-anser-evaluation.firebaseapp.com",
    "databaseURL": "https://subjective-anser-evaluation.firebaseio.com/",
    "projectId": "subjective-anser-evaluation",
    "storageBucket": "subjective-anser-evaluation.appspot.com",
    "messagingSenderId": "380898214934"
}
app = Flask(__name__)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
firebsevar = pyrebase.initialize_app(config)
db = firebsevar.database()

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(email, password)
                #user_id = auth.get_account_info(user['idToken'])
                #session['usr'] = user_id
                return render_template('home.html')
            except:
                unsuccessful = 'Please check your credentials'
                return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')
@app.route('/test', methods=['POST', 'GET'])
def foo():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']

        email = request.form['emailID']

        ans = {"a1": first, "a2": second, "a3": third, "email": email}

        result = db.child("/answers").push(ans)

        # authvar = firebsevar.auth()
        # print(authvar.current_user)
        # result = firebasevar.post('/answers/', data=ans, params={'print': 'pretty'},
        #                           headers={'X_FANCY_HEADER': 'VERY FANCY'})
        # print(result)
    return render_template('first.html')
if __name__ == '__main__':
    app.run(debug=True)
