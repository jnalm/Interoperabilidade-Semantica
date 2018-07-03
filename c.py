import socket

s = socket.socket()         # Create a socket object
host = '25.53.45.20' # Get local machine name
port = 1241	          # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")
t = True
while (t):
	f = open('RECEBI.txt','wb')
	l = s.recv(1024)
    	f.write(l)
    	l = s.recv(1024)
    	f.close()
    	t = False