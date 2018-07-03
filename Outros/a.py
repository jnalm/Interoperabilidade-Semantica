#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import socket
import time
import MySQLdb
import subprocess

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "1234", db = "is")

cur = db.cursor()

doente = {
	"idDoente" : "",
	"idProcesso" : "",
	"morada" : "",
	"telefone" : "",
	"nome" : "",
	"sexo" : ""
}

pedido = {
	"idPedido" : "",
	"descricao" : "",
	"hora" : "",
	"data" : "",
	"idEpisode" : "",
	"idDoente" : "",
	"tipo" : "",
	"medico" : ""
}

atual = {
	"idPedido" : "",
	"idDoente" : "",
	"estado" : "",
	"relatorio" : ""
}

# Regista Doentes
def reg_doe(processo, morada, telefone, nome, sexo):
	cur.execute("INSERT INTO Doente VALUES(null, '" + str(processo) + "', '" + morada + "', '" + telefone + "', '" + nome + "', '" + sexo + "')")
	db.commit()

# Registar Pedido
def reg_ped(descricao, hora, data, idEpisode, idDoente, relatorio, estado, medico, tipo):
	cur.execute("INSERT INTO Pedido VALUES(null, '" + descricao + "', '" + hora + "', '" + data + "', '" + str(idEpisode) + "', '" + str(idDoente) + "', '" + relatorio + "', '" + estado + "', '" + medico + "', '" + tipo + "')")
	db.commit()

# Update Pedido
def upd_ped(estado):
	cur.execute("UPDATE Pedido SET estado = " + estado + " WHERE idPedido = " + str(pedido["idPedido"]))
	db.commit()

# Cancelar Pedido
def can_ped(idpedido, iddoente):
	get_info(idpedido, iddoente)
	cur.execute("UPDATE Pedido SET estado = 'CA' WHERE idPedido = " + str(idpedido))
	db.commit()

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
	

# REQUISIÇÃO DE EXAMES

# Relatório Exame Finalizado (CM) Slide 3/10
def gen_report(doente, pedido):
	report = "MSH|^~\&|B|B|A|A|" + pedido["data"] + "||ORM^O01|A" + pedido["data"] + "16000006775|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "|||||||||||\nPV1||O|RAD||||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|SC|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||CM||||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|||||||||||^^^||||||||||0||^^^" + pedido["data"] + "^^N||||||" 
	return report

# Relatório Exame Imagiologia Slide 2/10
def gen_report2(doente, pedido):
	report = "MSH|^~\&|A|A|B|B|" + pedido["data"] + "||ORM^O01|A" + pedido["data"] + "51000002533|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||" + doente["telefone"] + "|\nPV1||I|INT||||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|NW|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||||||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|||||||||||^^^|||CR|RXE||||||30||^^^" + pedido["data"] + "^^0||||||"
	return report

# Relatório Exame Imagiologia Cancelamento Slide 2/10
def gen_report3(doente, pedido):
	report = "MSH|^~\&|A|A|B|B|" + pedido["data"] + "||ORM^O01|A" + pedido["data"] + "51000002533|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||" + doente["telefone"] + "|\nPV1||I|INT||||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|CA|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||||||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|||||||||||^^^|||CR|RXE||||||||^^^" + pedido["data"] + "^^0||||||"
	return report

# Relatório Exame Imagiologia Cancelamento Slide 2/10
def gen_report4(doente, pedido):
	report = "MSH|^~\&|B|B|A|A|" + pedido["data"] + "||ORM^O01|A" + pedido["data"] + "51000002533|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||" + doente["telefone"] + "|\nPV1||I|INT||||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|CA|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||||||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|||||||||||^^^|||CR|RXE||||||||^^^" + pedido["data"] + "^^0||||||"
	return report

# Relatório em TX Slide 4/10
#def gen_report5(doente, pedido):
#	report = "MSH|^~\&|PACS|PACS|AIDA|AIDA|" + pedido["data"] + "||ORU^R01|treta|P|2.5\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "\nORC|RE|" + str(pedido["idPedido"]) + "|treta||CM|||||||^|||||||||^||||\nOBR|1|" + str(pedido["idPedido"]) + "^AIDA|treta|^|||||||||Observa\E\X E7\E\_\_E\XF5\E\es: Registo direto sem pedido (10854) - |||^||||||" + pedido["data"] + "|||" + doente["sexo"] + "|||||||" + pedido["medico"] + "^^^||||\nOBX|1|TX|||" + pedido["descricao"] + "||||||" + doente["sexo"] + "|||" + pedido["data"] + "|||||"
#	return report

# Relatório em PDF Slide 5/10
#def gen_report6(doente, pedido):
#	report = "MSH|^~\&|B|B|A|A|" + pedido["data"] + "||ORU^R01|treta|P|2.5|||AL\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "||||" + doente["morada"] + "||||||||" + doente["telefone"] + "\nPV1|||||||||||||||||||" + str(pedido["idEpisode"]) + "|||S\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(pedido["idEpisode"]) + "|" + doente["sexo"] + "\nORC|RE|" + str(pedido["idPedido"]) + "|treta||CM|||||||^|||||||||^||||\nOBR|1|" + str(pedido["idPedido"]) + "^A|treta|^|||||||||Observa\E\X E7\E\_\E\XF5\E\es: Registo direto sem pedido (10888) - |||^||||||" + pedido["data"] + "|||" + doente["sexo"] + "|||||||" + pedido["medico"] + "^^^||||\nOBX|1|PDF_BASE64|||" + pedido["descricao"] + "|||||||||" + pedido["data"]
#	return report

# Relatório Admissão Slide 6/10
#def gen_report7(doente, pedido):
#	report = "MSH|^~\&|AIDA|AIDA|PACS|PACS|" + pedido["data"] + "||ADT^A40|" + pedido["data"] + "|P|2.5|||AL EVN|A40||||||\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "|||" + doente["morada"] + "|||||||0|\nMRG|" + str(pedido["idEpisode"]) + "|\nPV1||URG|1|5|||||||||||||||treta|"
#	return report

# Relatório Admissão Slide 6/10
#def gen_report8(doente, pedido):
#	report = "MSH|^~\&|AIDA|AIDA|PACS|PACS|" + pedido["data"] + "||ADT^A40|" + pedido["data"] + "|P|2.5|||AL|EVN|A08||||||\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0\nPV1|||URG||||||||||||||||treta|" 
#	return report

# REQUISIÇÃO DE ANáLISES

# Relatório 1 Slide 7/10
#def gen_report9(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||OML^O21|A" + pedido["data"] + "|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0|\nPV1||URG|1|||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|NW|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||||^^^" + pedido["data"] + "||" + pedido["data"] + "|||medico|||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||"
#	return report

# Relatório 2 Slide 7/10
#def gen_report10(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||OML^O21|A" + pedido["data"] + "|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0|\nPV1||URG|1|||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|SC|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||CM||||" + pedido["data"] + "|||treta|||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||"
#	return report

# Relatório 3 Slide 7/10
#def gen_report11(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||OML^O21|A" + pedido["data"] + "|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0|\nPV1||URG|1|||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|SC|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|HC||^^^" + pedido["data"] + "||" + pedido["data"] + "|||medico|||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||"
#	return report

# Relatório 4 Slide 7/10
#def gen_report12(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||OML^O21|A" + pedido["data"] + "|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0|\nPV1||URG|1|||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|SC|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||IP||^^^" + pedido["data"] + "||" + pedido["data"] + "|||medico|||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||"
#	return report

# Relatório Cancelamento Slide 8/10
#def gen_report13(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||OML^O21|A" + pedido["data"] + "|P|2.5|||AL|\nPID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0|\nPV1||URG|1|||||||||||||||" + str(pedido["idEpisode"]) + "|\nORC|CA|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "||||^^^" + pedido["data"] + "|||medico|||" + pedido["data"] + "|\nOBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["descricao"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||"
#	return report

# Relatório em TX Slide 9/10
#def gen_report14(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||ORU^R01|treta|P|2.5 PID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|" + doente["sexo"] + "||||||||||0|\nOBR|01|" + str(doente["idProcesso"]) + "|" + str(doente["idProcesso"]) + "|" + pedido["tipo"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||\nOBX|1|ST|BODY||" + pedido["descricao"] + "||||||" + doente["sexo"] + "||^" + pedido["medico"]
#	return report

# Relatório em PDF Slide 10/10
#def gen_report15(doente, pedido):
#	report = "MSH|^~\&|CLINIDATA|CLINIDATA|AIDA|AIDA|" + pedido["data"] + "||ORU^R01|treta|P|2.5|||AL PID|||" + str(doente["idProcesso"]) + "||" + doente["nome"] + "||" + str(doente["idDoente"]) + "|||" + doente["morada"] + "||||||||" + str(pedido["idEpisode"]) + " PV1|||||||||||||||||||treta|||\nORC|SC|treta|treta||CM||||" + pedido["data"] + "OBR|01|" + str(pedido["idPedido"]) + "|" + str(pedido["idPedido"]) + "|" + pedido["tipo"] + "|U||" + pedido["data"] + "|||||||||||||||||||||||||||||||||||||||||\nOBX|1|PDF_BASE64|||" + pedido["descricao"] + "|||||||||" + pedido["data"]
#	return report

def escreve_pedido(iddoente, idpedido):
	get_info(iddoente, idpedido)
	file = open("Pedido_" + str(idpedido) + ".txt", "w")
	title = "Pedido_" + str(idpedido) + ".txt"
	st = gen_report2(doente, pedido)
	file.write(st)
	file.close()
	return title


def escreve_cancelamento(iddoente, idpedido):
	get_info(iddoente, idpedido)
	file = open("Cancelamento_" + str(idpedido) + ".txt", "w")
	title = "Cancelamento_" + str(idpedido) + ".txt"
	st = gen_report3(doente, pedido)
	file.write(st)
	file.close()
	return title

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

def ler(file):
	with open(file, "r") as content:
		s = ""
		for c in content:
			s = s + c
		return s

def get_estado(s):
	estado = s.split("|")
	atual["estado"] = estado[59]
	atual["idPedido"] = estado[56]
	atual["idDoente"] = estado[22]
	atual["relatorio"] = s

def send(file):
	s = socket.socket()
	t = True
	host = '25.52.24.57'
	port = 1241
	s.connect((host, port))
	f = open(file,'r')
	l = f.read(1024)
	while (t):
		s.send(l)
		f.close()
		t = False
	s.close()

def listarPedidos():
	cur.execute("SELECT * FROM Pedido")
	data = cur.fetchall()
	for i in data:
		print("{")
		print("     id : " + str(i[0]))
		print("     Descricao : " + str(i[1]))
		print("     Hora : " + str(i[2]))
		print("     Data : " + str(i[3]))
		print("     idDoente : " + str(i[5]))
		print("     Estado : " + str(i[7]))
		print("     Medico : " + str(i[8]))
		print("     Tipo : " + str(i[9]))
		print("}")

for i in range(0,1000):
	print("1 - Listar Pedidos\n2 - Inserir Doente\n3 - Inserir Pedido\n4 - Cancelar Pedido\n0 - Sair")
	choice = int(input('Inserir: '))
	if choice == 1:
		listarPedidos()
	elif choice == 2:
		print("Qual e o numero do processo?")
		processo = str(input())
		print("Qual a sua morada?")
		morada = input()
		print("Qual o seu telemóvel?")
		telefone = input()
		print("Qual o seu nome?")
		nome = input()
		print("Qual o seu genero?")
		sexo = input()
		reg_doe(processo, morada, telefone, nome, sexo)
	elif choice == 3:
		print("Insira uma descricao:")
		descricao = raw_input()
		print("Insira a hora atual:")
		hora = raw_input()
		print("Insira a data de hoje:")
		data = raw_input()
		print("Insira o ID do Episódio:")
		idEpisode = str(input())
		print("Insira o ID do Doente:")
		idDoente = str(input())
		print("Insira o Medico responsavel:")
		medico = raw_input()
		print("Insira o tipo de tratamento:")
		tipo = raw_input()
		reg_ped(descricao, hora, data, idEpisode, idDoente, 'Inexistente', 'Em espera', medico, tipo)
		lastIdReq = getLastId("request")
		escreve_pedido(str(idDoente), str(lastIdReq))
		temp = gen_report2(doente, pedido)
		lastIdWL = getLastId("worklist")
		insert_report(lastIdWL, lastIdReq, temp)
		file = escreve_pedido(idDoente, lastIdReq)
		send(file)
	elif choice == 4:
		print("Insira o ID do Pedido:")
		idPedido = str(input())
		print("Insira o ID do Doente")
		idDoente = str(input())
		get_info(idDoente, idPedido)
		can_ped(idPedido, idDoente)
		lastIdReq = getLastId("request")
		lastIdWL = getLastId("worklist")
		escreve_cancelamento(idDoente, idPedido)
		temp = gen_report3(doente, pedido)
		insert_report(lastIdWL, lastIdReq, temp)
		file = escreve_cancelamento(idDoente, idPedido)
		send(file)
	else:
		quit()