

from flask import Flask, request, make_response, redirect
from flask import render_template
import json
import uuid
from common import loadlist, savelist, returnindex, updateitem, validate_token


from google.oauth2 import id_token
from google.auth.transport import requests



app = Flask(__name__)
CLIENT_ID="915555552081-gat5pr89plv84pjhbr5f6ind991t95bl.apps.googleusercontent.com"

@app.route('/', methods=['GET', 'POST'])
@app.route('/list.html',methods=['GET', 'POST'])
def shoppinglist():
    user = {'username': 'alex'}
    username=""
    edititem=None
	
    shoppinglist=loadlist('list.json',user['username'])

    if 'session_token' in request.cookies:
        print request.cookies['session_token']
        print validate_token( request.cookies['session_token'],CLIENT_ID)
	token, userid, username,  authorised = validate_token( request.cookies['session_token'],CLIENT_ID)
    else:
	print "not authenticated"
	authorised=False

    if not authorised:
	return "<p>Access Denied</p><a href=\"/login.html\">Try again</a>"


    if request.method=='POST':
	print request.form
	newid=uuid.uuid4().hex
	if len(request.form['newitem'])>0:
		shoppinglist.append({ "id" : newid, "userid" : user['username'], "item": request.form['newitem']})
		savelist('list.json', shoppinglist)	

    if request.method=='GET' and request.args.get('action')=='delete':
	del shoppinglist[returnindex(shoppinglist, request.args.get('itemid'))]	
	savelist('list.json', shoppinglist)


    if request.method=='GET' and request.args.get('action')=='update':
	shoppinglist=updateitem(shoppinglist,  request.args.get('itemid'),  request.args.get('newitem'))
        savelist('list.json', shoppinglist)

    if request.method=='GET' and request.args.get('action')=='edit':
        edititem=request.args.get('itemid')


    return render_template('list.html', title='Home', user=username, shoppinglist=shoppinglist, edititem=edititem)



@app.route('/login.html',methods=['GET', 'POST'])
def login():


    return render_template('login.html', title='Shopping List Login Page', user=None)


@app.route('/authorise.html',methods=[ 'POST'])
def authorise():
    token=request.form['idtoken']
#    token="x"
    token, userid, username, authorised = validate_token(token, CLIENT_ID)

    if authorised:
        response = make_response(redirect('/list.html'))
        response.set_cookie('session_token', token)
        return response
    else:

        return "permission denied"

