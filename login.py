from flask import Flask, request, make_response, redirect
from flask import render_template
import json
import uuid
from google.oauth2 import id_token
from google.auth.transport import requests

app = Flask(__name__)


CLIENT_ID="322716948446-jjiki9vlg8j5rontfumc9o246es0c0da.apps.googleusercontent.com"

def validate_token(token, CLIENT_ID):
	authorised=False
	try:
    		# Specify the CLIENT_ID of the app that accesses the backend:
    		idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)


	    	if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        		raise ValueError('Wrong issuer.')
		print idinfo

    		userid = idinfo['sub']
		authorised=True
	
	except ValueError:
    	# Invalid token
		print "not authorised"
		userid=None
    		pass
	
	return token, userid, authorised


@app.route('/', methods=['GET', 'POST'])
@app.route('/login.html',methods=['GET', 'POST'])
def login():


    return render_template('login.html', title='Shopping List Login Page', user=None)


@app.route('/authorise.html',methods=[ 'POST'])
def authorise():
    token=request.form['idtoken']
#    token="x"
    token, userid, authorised = validate_token(token, CLIENT_ID)

    if authorised:
    	response = make_response(redirect('/login.html'))
    	response.set_cookie('session_token', token)
    	return response
    else:

    	return "permission denied"

