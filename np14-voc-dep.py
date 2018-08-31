# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob, datetime

sources = glob.iglob("tokens/*.csv")
dep = "deputesAssnat.csv"
output = "richesse-vocabulaire.csv"

for source in sources:
	f1 = open(source)
	lignes = csv.reader(f1)

	mots = []

	for ligne in lignes:
		mots.append(ligne[6])

	f2 = open(dep)
	deputes = csv.reader(f2)

	for depute in deputes:
		if ligne[0] == depute[0]:
			nom = depute[1]
			prenom = depute[2]
			circ = depute[3]
			parti = depute[4]
	diversite = len(set(mots))/len(mots)
	print(ligne[0],diversite)

	henri = open(output, "a")
	bourassa = csv.writer(henri)
	bourassa.writerow([ligne[0],prenom,nom,circ,parti,len(mots),len(set(mots)),diversite])