#!/usr/bin/python3

import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SAVE IP and port that I want to scan
host = "194.168.1.73"
port = 443

# Function responsible for the scan
def portscanner(port):

	# Condition checks if it is possible to connect to the specified port
	# connect_ex, if it fails, returns that the port is closed.
	if sk.connect_ex((host,port)):
		print("Port %d is closed" % (port))
	else:
		print("Port %d is open" % (port))

# Call function "portscanner"
portscanner(port)