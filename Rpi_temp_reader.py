import os, glob
import time
import sys

# initialize the device
# Run sudo su first to be logged in as root.

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
#print(os.listdir(base_dir))

device_folder = glob.glob(base_dir + '28*')[0]

device_file = device_folder + '/w1_slave'

def read_raw_temp():
	f =  open(device_file , 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_raw_temp()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(30)
		lines = read_raw_temp()
	equal_pos = lines[1].find('t=')

	if equal_pos != -1:
		temp_string = lines[1][equal_pos+2:]
		temp_C = float(temp_string)/ 1000.
		temp_F = temp_C * 9./5. + 32.
#                print temp_C,temp_F
                return temp_C, temp_F
        #time.sleep(1)

def avg_temp():
    tempC = 0.0
    count= 0
    tempF = 0.0
    tC = []
    tF = []
    timeout = 31. # float( time.strftime("%Y,%m,%d,%H,%M").split(',')[4]) + 1. 
    while count < timeout:
        tC.append(tempC)
        tF.append(tempF)
        tempC += read_temp()[0]
        tempF += read_temp()[1]
        count += 1
#        print count
    temp_CC = sum(tC)/len(tF)#tempC/float(count)
    temp_FF = sum(tF)/len(tF)#tempF/float(count)
    return temp_CC,temp_FF
#while True:
#	print read_temp()[0]
#	time.sleep(1)
