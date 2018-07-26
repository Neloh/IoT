'''
Created: 18 July 2018
Author: Sibonelo
Collaborators: Peet, Promise

Ran: In python 2.x in order to be able to access 
the web module. python ws.py

'''
import web
import Rpi_temp_reader
import time

urls = (
    '/(.*)', 'Rpi_Temp'
)

app = web.application(urls, globals())

class Rpi_Temp:
    def GET(self, name):
        '''
          This function calls the temperature function in
          the script Rpi_temp_reader.py and 
            Args: None

          returns temp in degrees Celcius
        Under construction: the function is supposed to sleep for
        1 ms before returning tempC again

        '''
        global temp_CC,temp_FF
        while True:
            temp_CC, temp_FF = Rpi_temp_reader.avg_temp()
            return temp_CC,temp_FF
            time.sleep(1)

if __name__ == "__main__":
    app.run()
   
   
# Done now, run the web client part of the code in your desktop CLI
# using the IP address of this server ( Raspberry PI IP address).
# Check wcl.py in the github link https://github.com/Neloh/IoT

# The README.md file should be enough to help you deploy the code
# in your own environment.

