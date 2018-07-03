import os
import json
import pprint

orcid_prof = "0000-0003-4121-6169"

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

file = open("Temp.txt", "r")
orcids = file.read().split("\n")
file.close()

def addLista(orcid):
	file = open("Temp.txt", "a")
	file.write("\n")
	file.write(orcid)
	file.close()
	orcids.append(orcid)

def removeLista(orcid):
	orcids.remove(orcid)

for i in range(0,10):
	print("1 - Exportar Trabalhos\n2 - Exportar Trabalhos da Lista\n3 - Adicionar ORCID\n4 - Eliminar ORCID\n5 - Listar ORCID\n0 - Sair")
	choice = int(input('Inserir: '))
	if choice == 1:
		print("Insira o ORCID:")
		orcid = input()
		works = os.popen("curl -X GET --header \"Accept: application/json\" \"https://pub.orcid.org/v2.1/" + orcid + "/works\"").read()
		file = open("Works_" + str(orcid) + ".json", "w")
		file.write(works)
		file.close()
		orcs = open("Temp.txt", "w")
		orcs.write("%s" % orcid)
		orcs.close()		
		os.popen("start file:///C:/Users/JoãoNuno/Desktop/Universidade/Mestrado/CadeirasN/IS/ORCID%20Organizer/IS/mainpage.html").read()
		# > final_json" + str(i) + ".json
	if choice == 2:
		for myid in orcids:
			works = os.popen("curl -X GET --header \"Accept: application/json\" \"https://pub.orcid.org/v2.1/" + str(myid) + "/works\"").read()
			file = open("Works_" + str(myid) + ".json", "w")
			file.write(works)
			file.close()
		os.popen("start file:///C:/Users/JoãoNuno/Desktop/Universidade/Mestrado/CadeirasN/IS/ORCID%20Organizer/IS/mainpage.html").read()
	if choice == 3:
		print("Insira o ORCID que pretende adicionar:")
		orcid = input()
		addLista(orcid)
	if choice == 4:
		print("Insira o ORCID que pretende eliminar:")
		orcid = input()
		removeLista(orcid)
	if choice == 5:
		print(orcids)
	if choice == 0:
		quit()