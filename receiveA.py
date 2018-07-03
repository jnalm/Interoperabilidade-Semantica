import socket
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="is")
cur = db.cursor()

atual = {
	"idPedido" : "",
	"idDoente" : "",
	"estado" : "",
	"relatorio" : ""
}

def getLastId(type):
	sttReq = "SELECT idPedido FROM Pedido ORDER BY idPedido DESC LIMIT 1"
	sttWL = "SELECT idWorklist FROM Worklist ORDER BY idWorklist DESC LIMIT 1"
	if type == "request":
		cur.execute(sttReq)
	else:
		cur.execute(sttWL)
	data = cur.fetchall()
	for i in data:
		lastId = i[0]
	return lastId

def insert_report(idwl, idped, report):
	cur.execute("UPDATE Worklist SET relatorio = '" + str(report) + "' WHERE idWorklist = '" + str(idwl) + "' AND idPedido = '" + str(idped) + "'")
	db.commit()

def update_estado():
	cur.execute("UPDATE Pedido SET estado = '" + atual["estado"] + "', relatorio = '" + atual["relatorio"] + "' WHERE idPedido = " + atual["idPedido"])
	db.commit()

def get_estado(s):
	estado = s.split("|")
	atual["estado"] = estado[59]
	atual["idPedido"] = estado[56]
	atual["idDoente"] = estado[22]
	atual["relatorio"] = s

def receive():
	s = socket.socket()
	host = '25.53.45.20'
	port = 1242
	s.bind((host, port))
	s.listen(5)
	for i in range(0,10000):
		c, addr = s.accept()
		f = open("MensagemRecebida_" + str(i) + ".txt","w")
		l = c.recv(1024).decode()
		f.write(l)
		get_estado(l)
		update_estado()
		lastIdReq = getLastId("request")
		lastIdWL = getLastId("worklist")
		insert_report(lastIdWL, lastIdReq, l)
		f.close()
	s.shutdown(socket.SHUT_WR)

def main():
	receive()

if __name__=="__main__":
	main()