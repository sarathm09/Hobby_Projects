__author__ = 'T90'
__version__ = '1.0.0'

import socket

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
	msg = raw_input('Msg : ')
	s.send(msg)
	reply = s.recv(1024)
	print 'Rec : ' + reply

s.close()