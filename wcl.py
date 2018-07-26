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
url = 'http://10.51.6.112:8080/temp' # The raspberry Pi as the 
# web service.
while True:
	with urllib.request.urlopen(url) as response:
		avg_temperature_C, avg_temperature_F =\
		 response.read().decode('utf-8').strip('(').strip(')').split(',')
		
		#temperature = temperature[:-1] # strip the last entry off the string
		#temperature = temperature[1:] # strip the first entry off 
		
		#avg_temperature_C, avg_temperature_F = temperature.split(',')
		print("AVG Temp Celcius= {}, AVG Temp Fahrenheit= {}".format(float(avg_temperature_C),\
		 float(avg_temperature_F)))

		proc_string = "CALL tdata_db_2.Weather_Log_Create({0}, {1})".format(avg_temperature_C,\
		 avg_temperature_F)

		cursor =  session.cursor()
		cursor.execute(proc_string);

