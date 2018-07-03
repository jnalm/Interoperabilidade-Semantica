import os
import json
import pprint
import timeit
import re

orcid_JMachado = "0000-0003-4121-6169"
orcid_HPeixoto = "0000-0003-3957-2121"

def print_init():
	print("")
	print(" ---------------------------------------------------")
	print(" ---------------------------------------------------")
	print(" -                                                 -")
	print(" -  ====================     ====================  -")
	print(" -  ====================     ====================  -")
	print(" -          ====             ====                  -")
	print(" -          ====             ====                  -")
	print(" -          ====             ====================  -")
	print(" -          ====             ====================  -")
	print(" -          ====                             ====  -")
	print(" -          ====                             ====  -")
	print(" -  ====================     ====================  -")
	print(" -  ====================     ====================  -")
	print(" -                                                 -")
	print(" ---------------------------------------------------")
	print(" ---------------------------------------------------")
	print(" -                                                 -")
	print(" -      *** Interoperabilidade Semantica ***       -")
	print(" -                                                 -")
	print(" ---------------------------------------------------")
	print(" ---------------------------------------------------")
	print("")

print_init()

pattern = re.compile("([0-9]{4}-){3}[0-9]{4}")

orcids = []

def export():
	file = open("Temp.txt", "a")
	if os.stat("Temp.txt").st_size != 0:
		file.write("\n")
	for orcid in orcids:
		file.write(orcid)
		if orcid != orcids[len(orcids) - 1]:
			file.write("\n")
	file.close()

def removeNewLines():
	f = open("Temp.txt", "r+")
	l = [l for l in f.readlines() if l.strip()]
	for line in l:
		f.write(line)
	f.close()


def removeLista(orcid):
	orcids.remove(orcid)

while True:
	print("1 - Listar ORCIDs\n2 - Adicionar ORCID\n3 - Remover ORCID\n4 - Exportar Trabalhos\n5 - Limpar Lista\n0 - Sair")
	choice = int(input('Inserir: '))
	if choice == 1:
		print(orcids)
		print("")
		continue
	if choice == 2:
		print("Insira o ORCID que pretende adicionar: ")
		orcid = input()
		if pattern.match(orcid):
			orcids.append(orcid)
			print("\nORCID acrescentado à lista!\n")
		else:
			print("\nORCID inválido!\n")
		continue
	if choice == 3:
		print("Insira o ORCID que pretende eliminar: ")
		orcid = input()
		if pattern.match(orcid):
			removeLista(orcid)
			print("ORCID removido!\n")
		else:
			print("ORCID inválido!\n")
		continue
	if choice == 4:
		export()
		#removeNewLines()
		start_time = timeit.default_timer()
		for myid in orcids:
			works = os.popen("curl -X GET --header \"Accept: application/json\" \"https://pub.orcid.org/v2.1/" + str(myid) + "/works\"").read()
			file = open("Works_" + str(myid) + ".json", "w")
			file.write(works)
			file.close()
		elapsed = timeit.default_timer() - start_time
		time = round(elapsed, 3)
		time_str = str(time)
		file = open("Time.txt", "w")
		file.write(time_str)
		file.close()
		orcids = []
		continue
	if choice == 5:
		fd = False
		while (fd != True):
			c = input("Tem a certeza que deseja apagar a lista? Sim[s] Não[n]: ")
			print("")
			if c == "s":
				orcids = []
				open('Temp.txt', 'w').close()
				open('Time.txt', 'w').close()
				print("Lista Apagada!\n")
				fd = True
				continue
			if c == "n":
				fd = True
				print("Operação cancelada!\n")
				continue
			else:
				print("Comando não reconhecido!\n")
		continue
	if choice == 0:
		quit()
	else:
		print("Comando inválido!\n")


	#if choice == 1:
	#	print("Insira o ORCID:")
	#	orcid = input()
	#	start_time = timeit.default_timer()
	#	works = os.popen("curl -X GET --header \"Accept: application/json\" \"https://pub.orcid.org/v2.1/" + orcid + "/works\"").read()
	#	file = open("Works_" + str(orcid) + ".json", "w")
	#	file.write(works)
	#	file.close()
	#	orcs = open("Temp.txt", "w")
	#	orcs.write("%s" % orcid)
	#	orcs.close()
	#	elapsed = timeit.default_timer() - start_time
	#	time = round(elapsed, 3)
	#	time_str = str(time)
	#	file = open("Time.txt", "w")
	#	file.write(time_str)
	#	file.close()
		# os.popen("start file:///C:/Users/Luismf20/Desktop/Frontend/Frontend/index.html").read()
		# > final_json" + str(i) + ".json