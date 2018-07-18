##!/usr/bin/python
#import urllib2
import urllib.request
import time
#Setup URL
#url = 'http://192.168.1.126:8080/teradata'
url = 'http://10.51.6.90:8080/teradata' # The raspberry Pi as the 
# web service.
while True:
	with urllib.request.urlopen(url) as response:
		r = response.read()
		print(r)
		time.sleep(1)
