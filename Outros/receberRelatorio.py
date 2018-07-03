from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import MySQLdb
import hl7

db = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="pedidos")


def enviaConfirmacao():
	server_ip = '25.52.24.57'
	port_number = 5004

	replySocket = socket(AF_INET, SOCK_DGRAM)
	myMessage = "ACK"

	replySocket.sendto(myMessage.encode('utf-8'), (server_ip, port_number))

def recebeRelatorio():
	hostName = gethostbyname( '0.0.0.0' )
	PORT_NUMBER = 5003
	SIZE = 10000

	mySocket = socket( AF_INET, SOCK_DGRAM )
	mySocket.bind( (hostName, PORT_NUMBER) )

	print ("Test server listening on port {0}\n".format(PORT_NUMBER))