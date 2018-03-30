from flask import Flask, request
from flask import render_template
import json
import uuid


app = Flask(__name__)


def loadlist(filename,user):
      data = json.load(open(filename))
      filtered_data=list()
      for i in data:
	  if i['userid']==user:
		  filtered_data.append(i.copy())	
      return filtered_data
	
def savelist(filename, shoppinglist):
	with open(filename, "w") as outfile:
    		json.dump(shoppinglist, outfile, indent=4)

def returnindex(shoppinglist,itemid):
	for i,d in enumerate(shoppinglist):	
		if d['id']==itemid:
			return i
	return None

def updateitem(shoppinglist, itemid, newvalue):
	i=returnindex(shoppinglist, itemid)
	shoppinglist[i]['item']=newvalue
	return shoppinglist
		
			
@app.route('/', methods=['GET', 'POST'])
@app.route('/list.html',methods=['GET', 'POST'])
def shoppinglist():
    user = {'username': 'alex'}

    edititem=None

    shoppinglist=loadlist('list.json',user['username'])

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




    return render_template('list.html', title='Home', user=user, shoppinglist=shoppinglist, edititem=edititem)


