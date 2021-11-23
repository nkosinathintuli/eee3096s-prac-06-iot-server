#!/usr/bin/env python
from csv import DictReader
import threading
import datetime
import socket
import csv  
import os 

TCP_IP = ''
P1_IP = '192.168.137.105'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
global temp_ADC
temp_ADC = -1
global LDR_ADC
LDR_ADC = -1

global counter
counter=time.time()
e=datetime.datetime.now()
global tim
tim = e.strftime("%H:%M:%S")

#Receives data from client

def recieving(cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)
	conn, addr = s.accept()
	print('Connection address:', addr)
	while 1:
		if(cmd=="0"):
			break
		data = conn.recv(BUFFER_SIZE)
	    if not data: continue
		print("received data:", data)
		conn.send(data)  # echo
		conn, addr = s.accept()
	conn.close()


def send_cmd(cmd):
	print("Sending...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((P1_IP, TCP_PORT))
	s.send(cmd)
	data = s.recv(BUFFER_SIZE)
	s.close()
	print("received data:", data)
	pass
#save new data to CSV file
def add(row):
    with open('sensorlog.csv', 'a',encoding='UTF8',newline='') as csvfile: 
        writer1 = writer(csvfile) 
        writer1.writerow(row)
        csvfile.close()
#create a new CSV file
def create():
    header = ['Date', 'Time', 'Temparature', 'LDR']
    with open('sensorlog.csv', 'w',encoding='UTF8',newline='') as csvfile: 
        writer1 = writer(csvfile) 
        writer1.writerow(header)
        csvfile.close()




#print the last 10 samples items
def logcheck():
    with open('sensorlog.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        count=1
        print("The last 10 items to be samples are listed")
        for row in csv_dict_reader:
            print(count,row['Date'], row['Time'],row['Temparature'],row['LDR'],flush=True)
            count=count+1
            if(count>=11):
                break
#checks if the pi samples or not
def status(active1):
    if(active1=="Sensor On"):
        print("The last data was sampled at:",tim,flush=True)
    elif(active1=='Sensor Off'):
        print("The Pi is not sampling",flush=True)

