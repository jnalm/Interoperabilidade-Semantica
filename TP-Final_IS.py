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

orcids = []

def addLista(orcid):
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
		out = os.popen("Works_" + str(i) + ".json | py -m json.tool > final_json" + str(i) + ".json").read()
		# > final_json" + str(i) + ".json
	if choice == 2:
		for i in orcids:
			works = os.popen("curl -X GET --header \"Accept: application/json\" \"https://pub.orcid.org/v2.1/" + i + "/works\"").read()
			file = open("Works_" + str(i) + ".json", "w")
			file.write(works)
			file.close()
			out = os.popen("Works_" + str(i) + ".json | py -m json.tool > final_json" + str(i) + ".json").read()
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
	else:
		print("Opção Inválida!")