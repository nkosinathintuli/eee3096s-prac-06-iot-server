#!/usr/bin/env python

import threading
import datetime
import socket
import csv  
import os 

TCP_IP = ''
P1_IP = '192.168.137.105'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

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
	print("Closed")

def send_cmd(cmd):
	print("Sending...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((P1_IP, TCP_PORT))
	s.send(cmd)
	data = s.recv(BUFFER_SIZE)
	s.close()
	print("received data:", data)
	pass

def savelog(log):
	e = datetime.datetime.now()
	date = e.strftime("%d/%m/%Y")
	time = e.strftime("%H:%M:%S")
	data = [date, time, log[0], log[1]]
	with open('sensorlog.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(data)
	print("Saved")

def create():
	header = ['date', 'time', 'temparature', 'ldr']
	with open('sensorlog.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(header)
	print("Created")

def delete():
	if os.path.exists("sensorlog.csv"):
		os.remove("sensorlog.csv")
		print("Deleted")
	else:
		print("The file does not exist")

def download():
	path = "sensorlog.csv"
	return send_file(path, as_attachment=True)

