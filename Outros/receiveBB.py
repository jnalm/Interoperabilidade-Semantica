import socket
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="luismf_20", db="is_systemb")

atual = {
	"idPedido" : "",
#	"descricao" : "",
#	"hora" : "",
#	"data" : "",
#	"idEpisode" : "",
	"idDoente" : "",
	"estado" : ""
#	"tipo" : "",
#	"medico" : "",
#	"idProcesso" : "",
#	"morada" : "",
#	"telefone" : "",
#	"nome" : "",
#	"sexo" : ""
}

def analisa_mensagem(s):
	mylist = s.split("||")
	tempidD = mylist[5]
	tempidP = mylist[22]
	temp = tempidD.split("|")
	temp2 = tempidP.split("|")
	idD = temp[0]
	idP = temp2[4]
	atual["idPedido"] = idP
	atual["idDoente"] = idD
	myData = s.split("|")
	finalData = myData[9]
	myfinalData = finalData.split("A")
	atual["data"] = myfinalData[1]
	myIDprocesso = s.split("|||")
	finalIDprocesso = myIDprocesso[2]
	IDprocesso = finalIDprocesso.split("||")
	atual["idProcesso"] = IDprocesso[0]
	myIDnome = s.split("||")
	atual["nome"] = myIDnome[4]
	finalSexo = myIDnome[5].split("|")
	atual["sexo"] = finalSexo[1]
	myIDEpisode = s.split("|")
	atual["idEpisode"] = myIDEpisode[53]
	atual["descricao"] = "Exame realizado com sucesso"

def update_worklist(idPedido, file, idDoente, status):
	if str(status) == "NW":
		cur.execute("INSERT INTO Worklist VALUES (null, idPedido, file, idDoente, status)")
	else:
		cur.execute("UPDATE Worklist SET status = '" + str(status) + "' WHERE idPedido = '" + str(idPedido) + "'")
	cur.commit()

def receive():
	s = socket.socket()
	host = '25.52.24.57' 
	port = 1241	          

	s.bind((host, port))
	s.listen(5)
	for i in range (0, 10000):
		c, addr = s.accept()
		if i == 0:
			print("Olha chegou uma!")
		else:
			print("Olha outra!")
		#f = open("MensagemRecebida_" + str(i) + ".txt","w")
		l = c.recv(1024).decode()
		print(l)
		#f.write(l)
		analisa_mensagem(l)
		update_worklist(atual["idPedido"], l, atual["idDoente"], atual["estado"])
		#f.close()
	s.shutdown(socket.SHUT_WR)

def main():
	receive()

if __name__=="__main__":
	main()