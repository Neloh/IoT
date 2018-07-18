import os, glob
import time
# initialize the device
# Run sudo su first to be logged in as root.
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/devices/'
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
		time.sleep(0.2)
		lines = read_raw_temp()
	equal_pos = lines[1].find('t=')
	if equal_pos != -1:
		temp_string = lines[1][equal_pos+2:]
		temp_C = float(temp_string)/ 1000.
		temp_F = temp_C * 9/5. + 32.
		return temp_C, temp_F
#while True:
#	print(read_temp())
#	time.sleep(1)