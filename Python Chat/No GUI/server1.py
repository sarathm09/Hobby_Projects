__author__ = 'T90'
__version__ = '1.0.0'

import socket

HOST = 'localhost'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print 'connected by ' + repr(addr)

while True:
	data = conn.recv(1024)
	print 'Rec : ' + data
	if not data: break
	reply = raw_input('Reply : ')
	conn.sendall(reply)

conn.close()