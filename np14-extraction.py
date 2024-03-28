# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob, requests, datetime, locale
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, '')

commissions = {
	"cap-41-1": "Commission de l'administration publique",
	"capern-41-1": "Commission de l'agriculture, des pêcheries, de l'énergie et des ressources naturelles",
	"cat-41-1": "Commission de l'aménagement du territoire",
	"can-41-1": "Commission de l'Assemblée nationale",
	"cce-41-1": "Commission de la culture et de l'éducation",
	"cet-41-1": "Commission de l'économie et du travail",
	"cfp-41-1": "Commission des finances publiques",
	"ci-41-1": "Commission des institutions",
	"crc-41-1": "Commission des relations avec les citoyens",
	"csss-41-1": "Commission de la santé et des services sociaux",
	"cte-41-1": "Commission des transports et de l'environnement"
}

entete = {
	"User-Agent":"Jean-Hugues Roy, UQAM - 514/987-3000, poste 6102",
	"From":"roy.jean-hugues@uqam.ca"
}

fichiersTRAVAUX = glob.iglob("sources/*.htm")
fichiersPRESSE = glob.iglob("sources/*.html")

n = 0

for fichierTRAVAUX in fichiersTRAVAUX:
	print(fichierTRAVAUX)
	p = BeautifulSoup(open(fichierTRAVAUX),"html.parser")
	liens = p.find("table", id="grilleResultats").find_all("a")
	comm = []
	for lien in liens:
		n += 1
		lien = lien["href"]
		# print(n,lien)
		l = lien.split("/")
		# print(l[5])
		if l[5] == "assemblee-nationale":
			assnat = "Assemblée nationale"
		else:
			for commission in commissions.items():
				if l[6] == commission[0]:
					assnat = commission[1]
		print(l[5],l[6],assnat)

		req = requests.get(lien)
		page = BeautifulSoup(req.text,"html.parser")

		titre = page.find_all("h1")
		titre = titre[1].text.strip()
		intitule = page.find("h2", class_="titre2TravauxParl").find_next("h2").text.strip()
		intitule = intitule.split("-")
		dateComplete = intitule[0].strip()
		dateComplete = dateComplete.replace("\r"," ")
		print(dateComplete)
		date1 = dateComplete.split(" ")
		print(date1)
		jour = date1[2]
		mois = date1[3]
		annee = date1[4]
		if len(jour) < 2:
			jour = "0{}".format(date1[2])
		mois = datetime.datetime.strptime(date1[3],"%B")
		mois = datetime.datetime.strftime(mois,"%m")
		date = "{}-{}-{}".format(annee,mois,jour)
		fichierOUTPUT = "extraction/{}{}{}-{}.csv".format(annee,mois,jour,l[5])
		# print(date)
		contenu = page.find("div",class_="imbGauche").find_all("p")
		# print(len(contenu))
		locuteur = ""
		for p in contenu:
			par = [lien,assnat,titre,annee,mois,jour,date]
			# print(p.text.strip())
			if p.find("b") in p:
				locuteur = ""
				for bold in p.find_all("b"):
					locuteur += bold.text + " "
				# print(locuteur)
				locuteur = locuteur.replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				paragraphe = p.text
				paragraphe = paragraphe[paragraphe.find(":")+1:].replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				# print(paragraphe)
			elif p.find("strong") in p:
				locuteur = ""
				for bold in p.find_all("strong"):
					locuteur += bold.text + " "
				# print(locuteur)
				locuteur = locuteur.replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				paragraphe = p.text
				paragraphe = paragraphe[paragraphe.find(":")+1:].replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				# print(paragraphe)
			else:
				paragraphe = p.text.replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				# print(paragraphe)
			# print(len(paragraphe),paragraphe)
			if len(paragraphe) > 0:
				if paragraphe[0] != "•" and paragraphe[0] != "(" and paragraphe != "..." and paragraphe != "…" and paragraphe != "" and paragraphe != "\n":
					par.append(locuteur)
					par.append(paragraphe)
					print(par)
					henri = open(fichierOUTPUT, "a")
					bourassa = csv.writer(henri)
					bourassa.writerow(par)

for fichierPRESSE in fichiersPRESSE:
	print(fichierPRESSE)
	p = BeautifulSoup(open(fichierPRESSE),"html.parser")
	liens = p.find_all("li", class_="icoHTML")
	for lien in liens:
		n += 1
		assnat = "Conférence de presse"
		lien = lien.a["href"]

		req = requests.get(lien)
		page = BeautifulSoup(req.text,"html.parser")

		titre = page.find_all("h1")
		titre = titre[1].text.strip()
		intitule = page.find("div", class_="conteneurColonnesImbriquees").find("h3").text.strip()
		intitule = intitule.split(",")
		dateComplete = intitule[0].strip()
		# print(dateComplete)
		date1 = dateComplete.split(" ")
		# print(date1)
		jour = date1[2]
		mois = date1[3]
		annee = date1[4]
		if len(jour) < 2:
			jour = "0{}".format(date1[2])
		mois = datetime.datetime.strptime(date1[3],"%B")
		mois = datetime.datetime.strftime(mois,"%m")
		date = "{}-{}-{}".format(annee,mois,jour)
		fichierOUTPUT = "extraction/{}{}{}-conf-presse.csv".format(annee,mois,jour)
		# print(date)
		# contenu = page.find("div", class_="conteneurColonnesImbriquees").find("div").find("div").find_all("p")
		contenu = page.find("div", class_="conteneurColonnesImbriquees").find_all("p")
		# print(len(contenu))
		locuteur = ""
		for p in contenu:
			par = [lien,assnat,titre,annee,mois,jour,date]
			# print(p.text.strip())
			if p.find("b") in p:
				locuteur = ""
				for bold in p.find_all("b"):
					locuteur += bold.text + " "
				# print(locuteur)
				locuteur = locuteur.replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				paragraphe = p.text
				paragraphe = paragraphe[paragraphe.find(":")+1:].replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				# print(paragraphe)
			elif p.find("strong") in p:
				locuteur = ""
				for bold in p.find_all("strong"):
					locuteur += bold.text + " "
				# print(locuteur)
				locuteur = locuteur.replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				paragraphe = p.text
				paragraphe = paragraphe[paragraphe.find(":")+1:].replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				# print(paragraphe)
			else:
				paragraphe = p.text.replace("\xa0"," ").replace("\n"," ").replace("  "," ").strip()
				# print(paragraphe, paragraphe[0])
			if len(paragraphe) > 0:
				if paragraphe[0] != "•" and paragraphe[0] != "(" and paragraphe != "..." and paragraphe != "…" and paragraphe != "" and paragraphe != "\n":
					par.append(locuteur)
					par.append(paragraphe)
					# print(paragraphe,"\n")
					print(par)
					henri = open(fichierOUTPUT, "a")
					bourassa = csv.writer(henri)
					bourassa.writerow(par)