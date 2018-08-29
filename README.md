## Nouveau Projet #14
# Les mots de la 41e législature
![](assnat.png)
### Méthodologie

Nous avons analysé tout ce qui a été dit par les élu.e.s de l'[Assemblée nationale](http://www.assnat.qc.ca/fr/index.html) au cours de la 41e législature.

#### Quand?
Entre le 8 avril 2014 et 11 mai 2018 (moment où il a fallu livrer pour *Nouveau Projet*).

#### Qui?
On s'intéresse uniquement à ce qui a été dit par les quelque [140 personnes ayant été élues au cours de la période étudiée (**deputesAssnat.csv**)](deputesAssnat.csv).

#### Où?
À trois endroits:
* Les [débats au Salon bleu](http://www.assnat.qc.ca/fr/travaux-parlementaires/assemblee-nationale/41-1/index.html)
* Les travaux au cours de l'une ou l'autre des différentes [Commissions parlementaires](http://www.assnat.qc.ca/fr/travaux-parlementaires/commissions/index.html)
* Les [conférences et points de presse des élus](http://www.assnat.qc.ca/fr/actualites-salle-presse/conferences-points-presse/index.html)

#### Comment?
Le travail s'est effectué en trois étapes:

* Il s'agissait d'abord de recopier les fichiers HTML des résultats de recherche pour les travaux parlementaires et les conférences et points de presse obtenus sur le site de l'Assemblée nationale et de les placer dans un répertoire appelé **sources**.
Voici deux exemples:
  * [**p10.htm**](p10.htm) -> la 10e page des résultats de recherche pour les travaux parlementaires et
  * [**presse2015.html**](presse2015.html) -> la page des résultats de recherche pour tous les points de presse de 2015.

* À partir de ces fichiers HTML, un premier script ([**np14-extraction.py**](np14-extraction.py)) faisait l'extraction de tout le texte contenu dans l'ensemble des **1&nbsp;344 fichiers de transcription** des travaux et points de presse de la période étudiée. En fait, pour chacun de ces fichiers, le script découpait la transcription en paragraphes. Pour chaque paragraphe, il enregistrait dans un fichier CSV les informations suivantes:
  * URL de la transcription
  * Instance («&nbsp;Assemblée nationale&nbsp;», «&nbsp;Commission&nbsp;...&nbsp;» ou «&nbsp;Conférence de presse&nbsp;»)
  * Titre du fichier HTML
  * Date
  * Locuteur
  * Texte des paroles prononcées
Voici un exemple d'un fichier CSV pour le [Journal des débats du 28 septembre 2017](20170928-assemblee-nationale.csv)
