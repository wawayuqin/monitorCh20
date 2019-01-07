# -*- coding:UTF-8 -*-
import serial 
import time
import os#用于清屏，os.system('cls') 
#串口工厂 
def serial_Factory(cmd,num): 
	serials = serial.Serial('/dev/ttyUSB0',9600) 
	serials.write(cmd) 
	argv = serials.read(3) 
        argv1 =serials.read(1) #读取高位和地位
	#print argv
	result = '' 
	result1 = ''
	hlen = len(argv) 
	hlen1 = len(argv1)
	for i in xrange(hlen): 
		hvol = ord(argv[i]) 
		hhex = '%02x' % hvol
	result += hhex + '' 
	for i in xrange(hlen1): 
		hvol = ord(argv1[i]) 
		hhex1 = '%02x' % hvol 
	result1 += hhex1 + '' 
	return result+ result1 
	#return cmd+'ok'


def get_ch20():
    cmd = '\xff\x01\x86\x00\x00\x00\x00\x00\x79'#向设备问询指令
    num = 9
    back = serial_Factory(cmd,num)
    b=str(int(back,16))+"微克/立方"
    return b
#if __name__ == '__main__':
#    while True:
	#get_ch20()
	#time.sleep(5)
        
