# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob, datetime

fichierDeputes = "deputesAssnat.csv"
fichiersINPUT = glob.iglob("extraction/*.csv")
fichierOUTPUT = "41eLegislature.csv"

for fichierINPUT in fichiersINPUT:
	print(fichierINPUT)
	f1 = open(fichierINPUT)
	lignes = csv.reader(f1)

	for ligne in lignes:
		date = datetime.datetime.strptime(ligne[6],"%Y-%m-%d")

		f2 = open(fichierDeputes)
		deputes = csv.reader(f2)
		next(deputes)

		for depute in deputes:
			# print(depute)
			# if depute[4] == "oui":
			# 	print(depute[5])
			# if depute[9] != "":
			# 	print(depute[0],depute[1],depute[2],depute[9])
			# print(nomVerif)
			if ligne[7] == depute[6]:
				# print(ligne[7], depute[6], ligne[8])
				if depute[4] == "oui":
					indep = datetime.datetime.strptime(depute[5],"%Y-%m-%d")
					if date > indep:
						parti = "Indépendant"
						print(depute[0],parti)
					else:
						parti = depute[3]
				else:
					parti = depute[3]
				discours = []
				discours.append(depute[0])
				discours.append(depute[1])
				discours.append(depute[2])
				discours.append(parti)
				discours.append(date)
				discours.append(ligne[3])
				discours.append(ligne[4])
				discours.append(ligne[5])
				discours.append(ligne[7])
				discours.append(ligne[8])
				discours.append(ligne[1])
				discours.append(ligne[0])

				print(discours)

				henri = open(fichierOUTPUT, "a")
				bourassa = csv.writer(henri)
				bourassa.writerow(discours)