##!/usr/bin/python
#import urllib2
import urllib.request
import time
import teradata
import pandas as pd

#Define application
udaExec = teradata.UdaExec (appName="TestAPP", version="1.0",
        logConsole=False)

#Open ODBC connection (the teradata dsn has to be setup in the local ODBC Administrator)
session = udaExec.connect(method="odbc", dsn="teradata",
        username="dbc", password="dbc")

#Setup URL
#url = 'http://192.168.1.126:8080/teradata'
url = 'http://10.51.6.90:8080/teradata' # The raspberry Pi as the 
# web service.
while True:
	with urllib.request.urlopen(url) as response:
		temperature = response.read()
		#print(temperature)
		#decode bytes to UTF8 format
		temperature = temperature.decode('utf-8')
		
		#Call stored procedure
		#temperature = 6
		humidity = 6
		proc_string = "CALL tdata_db_000.Weather_Log_Create({0}, {1})".format(temperature, humidity)

		cursor =  session.cursor()
		cursor.execute(proc_string);

		
