# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv
import pandas as pan

expression = input("Quelle expression on cherche? ")

fichINPUT = "41eLegislature.csv"
fichOUTPUT = "expressions.csv"

f1 = open(fichINPUT)
lignes = csv.reader(f1)

n = 0
mois = {'2014-04': 0, '2014-05': 0, '2014-06': 0, '2014-07': 0, '2014-08': 0, '2014-09': 0, '2014-10': 0, '2014-11': 0, '2014-12': 0, '2015-01': 0, '2015-02': 0, '2015-03': 0, '2015-04': 0, '2015-05': 0, '2015-06': 0, '2015-07': 0, '2015-08': 0, '2015-09': 0, '2015-10': 0, '2015-11': 0, '2015-12': 0, '2016-01': 0, '2016-02': 0, '2016-03': 0, '2016-04': 0, '2016-05': 0, '2016-06': 0, '2016-07': 0, '2016-08': 0, '2016-09': 0, '2016-10': 0, '2016-11': 0, '2016-12': 0, '2017-01': 0, '2017-02': 0, '2017-03': 0, '2017-04': 0, '2017-05': 0, '2017-06': 0, '2017-07': 0, '2017-08': 0, '2017-09': 0, '2017-10': 0, '2017-11': 0, '2017-12': 0, '2018-01': 0, '2018-02': 0, '2018-03': 0, '2018-04': 0, '2018-05': 0}

for ligne in lignes:
	n += 1
	if expression in ligne[4]:
		mois[ligne[2][:7]] += 1
		print(mois)

maintenant = pan.read_csv(fichOUTPUT)
print(maintenant)

nouveau = pan.Series(mois)
nouveau = nouveau.to_frame()
nouveau.columns = [expression]
print(nouveau)

desormais = pan.merge(maintenant, nouveau, left_on="mois", right_index=True)
print(desormais)

desormais.to_csv(fichOUTPUT, index=False)