#!/usr/bin/python3

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "194.168.1.73"
port = 443

def portscanner(port):
	if sk.connect_ex((host,port)):
		print("Port %d is closed" % (port))
	else:
		print("Port %d is open" % (port))

portscanner(port)