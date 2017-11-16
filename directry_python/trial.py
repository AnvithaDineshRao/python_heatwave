import sqlite3
import urllib.request,urllib.parse,urllib.error
import json
import time
import ssl
import os.path

#connect to sqlite3 database 
conn=sqlite3.connect('geodatass.sqlite')
cur=conn.cursor()
#URl which contains all the locations 
serviceurl = "http://python-data.dr-chuck.net/geojson?"
#This is for SSL handshake,this does not require it
scontext=None 
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

#Locate File 
scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'where_loc.data')
fh=open(filename)

#Start iterating the file to move down throug all the locations in the file
count = 0
for line in fh:
    if count > 200 : 
        print ('Retrieved 200 locations, restart to retrieve more')
        break
    address = line.strip()
    print ('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()), ))
    try:
        data = cur.fetchone()[0]
        print ("Found in database ",address)
        continue
    except:
        pass
#Creating URL by appending service URL and the location specified in the file
#Creates a new URl which has all the data related to that location
url = serviceurl + urllib.parse.urlencode({"sensor":"false", "address": address})
#Opens the URL
uh= urllib.request.urlopen(url, context=scontext)
#Read json content from the file ,which is in decoded format 
data = uh.read().decode()
#print("str(data))",str(data))
count=count+1

js = json.loads(str(data))
#writes that data to sqllite3
cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( (address),(data) ) )
conn.commit()

fh.close()
