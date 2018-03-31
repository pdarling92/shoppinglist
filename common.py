
import json
import logging
import urllib2

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


#def validate_token(token, CLIENT_ID):
#        authorised=False
#        try:
#                # Specify the CLIENT_ID of the app that accesses the backend:
#                idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
#
#
#                if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#                        raise ValueError('Wrong issuer.')
#                print idinfo
#
#                userid = idinfo['sub']
#                username = idinfo['given_name']
#                authorised=True

#        except ValueError:
#        # Invalid token
#                print "not authorised"
#                userid=None
#                username=None
#                return idinfo 

#        return token, userid, username, authorised

def check_tokeninfo(token):
	URL="https://www.googleapis.com/oauth2/v3/tokeninfo"
	contents=None
	userid=None
	username=None
        try: 	
		contents = json.loads(urllib2.urlopen(URL+"?id_token="+token).read())
	except:
		pass

	if not contents:
		return "not authorised", userid, username, False
	else:
		return token, contents['sub'], contents['given_name'], True
	

	
	

#print check_tokeninfo("xeyJhbGciOiJSUzI1NiIsImtpZCI6ImU5YjU2Y2ZjNjQwZDEyYmZmNDU0MDU1MzQwMmM3ZjE1N2Q0ODE4MDYifQ.eyJhenAiOiI5MTU1NTU1NTIwODEtZ2F0NXByODlwbHY4NHBqaGJyNWY2aW5kOTkxdDk1YmwuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI5MTU1NTU1NTIwODEtZ2F0NXByODlwbHY4NHBqaGJyNWY2aW5kOTkxdDk1YmwuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDQzNzY1Mzg1NjI0NDk4OTQ1NDAiLCJlbWFpbCI6InBkYXJsaW5ndG9uOTJAZ29vZ2xlbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6Il82aVVrb0gtOHNYZG9JZDJ4NEIwS3ciLCJleHAiOjE1MjI0OTIzNDcsImlzcyI6ImFjY291bnRzLmdvb2dsZS5jb20iLCJqdGkiOiJiMjZiMTFiNjJmN2JmMDAwYjNkYzBhODJjZmMxM2NiMDcwMDU5ZDhmIiwiaWF0IjoxNTIyNDg4NzQ3LCJuYW1lIjoiUGV0ZXIgRGFybGluZ3RvbiIsInBpY3R1cmUiOiJodHRwczovL2xoNS5nb29nbGV1c2VyY29udGVudC5jb20vLWUyUVVMTy0zTmdjL0FBQUFBQUFBQUFJL0FBQUFBQUFBQUFBL0FDTEd5V0E2bXhMalFUdW4tWlZleE82eDZrZXhPVkU3OHcvczk2LWMvcGhvdG8uanBnIiwiZ2l2ZW5fbmFtZSI6IlBldGVyIiwiZmFtaWx5X25hbWUiOiJEYXJsaW5ndG9uIiwibG9jYWxlIjoiZW4tR0IifQ.XBg9HFZCSG3CAWy_rOReqVMk-MUKAYuv8R7wNV4h6bthRYHrrfkhY9iKUrgfhXa3wGYdpwqzUfcGLu0qZ-qCeznKZD9ADznqksdQJnaFD-lu2_29LQTpRmcs9fnEdSayxhoAdoxHkmPr9aq5KMdowt5jWS_WWi-akAzBjcFkrwXrh5yOItg1KEPPC3R8hu-TMjqSYyfXFbALa99IaGtKlw4Qqwcd9Bjbvd8G1suT3QmiTwLoxPL6YC4PzFectLMJJMyY7wpbgw-2E6FV9wXfMhVe3fHYaEc7xG0eD3xcaGcehVMf07ebObAGzY9kU4tm7VTXWwjvpgnQUtKj5OL1ew")

#def validate_token(token, CLIENT_ID):
#        authorised=False
#        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
	
 #       return idinfo

