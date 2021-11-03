#!/usr/bin/env python

"""from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Wubba Lubba Dub-Dub!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)"""
 
import socket
 
TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
 
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	conn.send(data)  # echo
conn.close()


