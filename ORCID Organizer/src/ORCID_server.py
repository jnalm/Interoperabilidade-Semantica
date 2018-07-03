import os
import json
import time

day = 24 * 60 * 60
halfDay = day / 2
hour = day / 24
halfHour = hour / 2
minute = hour / 60
second_10 = minute / 6

print(" ------------------------------------------\n")
print("*** ORCID Organizer - Background Server ***\n")
print(" ------------------------------------------\n")

time.sleep(second_10)

while True:
	file = open("Temp.txt", "r")
	if os.stat("Temp.txt").st_size == 0:
		orcids = []
	else:
		orcids = file.read().split("\n")
	if not orcids:
		print("Sem ORCIDs para atualizar!\n")
	else:
		for orcid in orcids:
			works = os.popen("curl -X GET --header \"Accept: application/json\" \"https://pub.orcid.org/v2.1/" + str(orcid) + "/works\"").read()
			file = open("Works_" + str(orcid) + ".json", "w")
			file.write(works)
			file.close()
		print("")
		print("Artigos atualizados!\n")
	print("*** À espera para voltar a atualizar ***\n")
	time.sleep(second_10)
