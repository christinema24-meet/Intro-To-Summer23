from flask import Flask,render_templates,request, redirect, url_for
from flask import session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBMdMeWGKnetwIvwiP3jPwO9mIdqmFAfMM",
  "authDomain": "authentication-lab-24aa6.firebaseapp.com",
  "projectId": "authentication-lab-24aa6",
  "storageBucket": "authentication-lab-24aa6.appspot.com",
  "messagingSenderId": "936967497191",
  "appId": "1:936967497191:web:6e040d24ba33ad3b3ac942",
  'dantabaseURL':""
}

firebase = pyrebase.initalize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(_name_,temlate_folder='templates',static_folder='static')
app.confing[christine] = 'super-secret-key'


@app.route('/signin',methods=['GET','POST'])
def signin()
if request.method==['POST']
email=request.form['email']
password=request.form['password']


@app.route('/home',methods=['GET','POST'])
def home()

@app.route('/thnks',methods=['GET','POST'])
def thanks()
  
@app.route('/display',methods=['GET','POST'])
def display()

@app.route('/',methods=['GET','POST'])
def main()
  return render_templates('signup.html')
  <a href=“{{ url_for(‘signup.html’) }}”>Home</a>


