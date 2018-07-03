#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import MySQLdb
import subprocess

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "1234", db = "is")

cur = db.cursor()

atual = {
	"idPedido" : "",
	"descricao" : "",
	"hora" : "",
	"data" : "",
	"idEpisode" : "",
	"idDoente" : "",
	"tipo" : "",
	"medico" : "",
	"idProcesso" : "",
	"morada" : "",
	"telefone" : "",
	"nome" : "",
	"sexo" : ""
}

# Vai buscar info à BD
def get_info(iddoente, idpedido):
	cur.execute("SELECT idDoente FROM Doente WHERE idDoente = " + str(iddoente))
	data = cur.fetchall()
	for i in data:
		doente["idDoente"] = i[0]

	cur.execute("SELECT idProcesso FROM Doente WHERE idDoente = " + str(iddoente))
	data = cur.fetchall()
	for i in data:
		doente["idProcesso"] = i[0]

	cur.execute("SELECT morada FROM Doente WHERE idDoente = " + str(iddoente))
	data = cur.fetchall()
	for i in data:
		doente["morada"] = i[0]

	cur.execute("SELECT telefone FROM Doente WHERE idDoente = " + str(iddoente))
	data = cur.fetchall()
	for i in data:
		doente["telefone"] = i[0]

	cur.execute("SELECT nome FROM Doente WHERE idDoente = " + str(iddoente))
	data = cur.fetchall()
	for i in data:
		doente["nome"] = i[0]

	cur.execute("SELECT sexo FROM Doente WHERE idDoente = " + str(iddoente))
	data = cur.fetchall()
	for i in data:
		doente["sexo"] = i[0]

	cur.execute("SELECT idPedido FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["idPedido"] = i[0]

	cur.execute("SELECT descricao FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["descricao"] = i[0]

	cur.execute("SELECT hora FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["hora"] = i[0]

	cur.execute("SELECT data FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["data"] = i[0]

	cur.execute("SELECT idEpisode FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["idEpisode"] = i[0]

	cur.execute("SELECT idDoente FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["idDoente"] = i[0]

	cur.execute("SELECT tipo FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["tipo"] = i[0]

	cur.execute("SELECT medico FROM Pedido WHERE idPedido = " + str(idpedido))
	data = cur.fetchall()
	for i in data:
		pedido["medico"] = i[0]

def escreve(iddoente, idpedido):
	get_info(iddoente, idpedido)
	file = open('Test.txt', 'w')
	str = gen_report2(doente, pedido)
	file.write(str)
	file.close()
	return str

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

def ler(file):
	with open(file, "r") as content:
		s = ""
		for c in content:
			s = s + c
		return s

def send(file):
	command = 'scp ' + file + ' username@a:/path/to/destination'
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

def gen_report():
	report = "MSH|^~\&|B|B|A|A|" + atual["data"] + "||ORM^O01|A" + atual["data"] + "16000006775|P|2.5|||AL|\nPID|||" + str(atual["idProcesso"]) + "||" + atual["nome"] + "||" + str(atual["idDoente"]) + "|" + atual["sexo"] + "|||||||||||\nPV1||O|RAD||||||||||||||||" + str(atual["idEpisode"]) + "|\nORC|SC|" + str(atual["idPedido"]) + "|" + str(atual["idPedido"]) + "||CM||||" + atual["data"] + "|\nOBR|01|" + str(atual["idPedido"]) + "|" + str(atual["idPedido"]) + "|" + atual["descricao"] + "|||||||||||^^^||||||||||0||^^^" + atual["data"] + "^^N||||||" 
	return report

def gen_report4():
	report = "MSH|^~\&|B|B|A|A|" + atual["data"] + "||ORM^O01|A" + atual["data"] + "51000002533|P|2.5|||AL|\nPID|||" + str(atual["idProcesso"]) + "||" + atual["nome"] + "||" + str(atual["idDoente"]) + "|" + atual["sexo"] + "||||||||||" + atual["telefone"] + "|\nPV1||I|INT||||||||||||||||" + str(atual["idEpisode"]) + "|\nORC|CA|" + str(atual["idPedido"]) + "|" + str(atual["idPedido"]) + "||||||" + atual["data"] + "|\nOBR|01|" + str(atual["idPedido"]) + "|" + str(atual["idPedido"]) + "|" + atual["descricao"] + "|||||||||||^^^|||CR|RXE||||||||^^^" + atual["data"] + "^^0||||||"
	return report

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
	cur.execute("INSERT INTO Worklist VALUES (null, idPedido, file, idDoente, status)")
	cur.commit()

def escreveConcluido(s):
	file = open('ExameConcluido.txt', 'w')
	file.write(s)
	file.close()
	return s

def escreveCancelado(s):
	file = open('ExameCancelado.txt', 'w')
	file.write(s)
	file.close()
	return s

def receive():
	s = socket.socket()
	host = '25.53.45.20' 
	port = 1241	          

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

for i in range(0,1000):
	print "1 - Analisar Mensagem\n2 - Efetuar Exame\n3 - Cancelar Exame\n4 - Enviar Mensagem\n5 - Receber Mensagem\n0 - Sair"
	choice = int(input('Inserir: '))
	if choice == 1:
		print "Qual o nome do ficheiro que quer ler?"
		file = raw_input()
		s = ler(file)
		analisa_mensagem(s)
	elif choice == 2:
		s = gen_report()
		escreveConcluido(s)
		update_worklist(atual["idPedido"], s, atual["idDoente"], "CM")
	elif choice == 3:
		atual["descricao"] = "Exame cancelado por sua ordem"
		s = gen_report4()
		escreveCancelado(s)
		update_worklist(atual["idPedido"], s, atual["idDoente"], "CA")
	elif choice == 4:
		print "Indique o ficheiro que quer enviar para a Maquina A:"
		file = raw_input()
		send(file)
	elif choice == 5:
		receive()
	else:
		quit()