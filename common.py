import json
from google.oauth2 import id_token
from google.auth.transport import requests

CLIENT_ID="322716948446-jjiki9vlg8j5rontfumc9o246es0c0da.apps.googleusercontent.com"

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


def validate_token(token, CLIENT_ID):
        authorised=False
        try:
                # Specify the CLIENT_ID of the app that accesses the backend:
                idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)


                if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                        raise ValueError('Wrong issuer.')
                print idinfo

                userid = idinfo['sub']
		username = idinfo['given_name']
                authorised=True

        except ValueError:
        # Invalid token
                print "not authorised"
                userid=None
                pass

        return token, userid, username, authorised

