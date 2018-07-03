import socket

s = socket.socket()
t = True
host = '25.53.45.20'
port = 1241
s.bind((host, port))
s.listen(5)
f = open('Test.txt','rb')
l = f.read(1024)
while (t):
    c, addr = s.accept()
    c.send(l)
    f.close()
    t = False
s.shutdown(socket.SHUT_WR)
c.close()