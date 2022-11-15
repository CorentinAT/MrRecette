import requests
import ssl
import os
import urllib
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from random import randint

# Remplacer ces deux lignes par "webhook = <lien du webhook>"
load_dotenv()
webhook = os.getenv("webhook")

ssl._create_default_https_context = ssl._create_unverified_context # Éviter les erreurs de certification lors des recherches

# Base des liens pour naviguer
marmiton = "https://www.marmiton.org"
marmiton_recherche = "https://www.marmiton.org/recettes/recherche.aspx?"

# Options de pour la recherche Marmiton (incomplet -> voir les filtres sur le site marmiton)
options = {
    "dt": "platprincipal",       # Type de plat : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optionnel)
    "exp": 1,                    # Prix du plat : 1 -> Peu cher, 2 -> Moyen, 3 -> Plutôt cher (optionnel)
    "dif": 1,                    # Difficulté : 1 -> Très facile, 2 -> Facile, 3 -> Moyen, 4 -> Difficile (optionnel)
    "ttlt":45                    # Temps de préparation max : 15 -> -15min, 30 -> -30min, 45 -> -45min (optionnel)
}

#Recherche avec les options
options_url = urllib.parse.urlencode(options)
recherche_url = marmiton_recherche + options_url
resultat_html = urllib.request.urlopen(recherche_url).read()
soup = BeautifulSoup(resultat_html, 'html.parser')

# Aller sur un numéro de page aléatoire dans le résultat de la recherche
pages = soup.find_all('a', {'class':'SHRD__sc-1ymbfjb-1 MTkAM'})
no_page_aleatoire = randint(0,17) # Ligne à adapter (ou mettre un try) en fonction de la recherche
if no_page_aleatoire!=17:
    page_url = marmiton + pages[no_page_aleatoire]['href']
    resultat_html = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(resultat_html, 'html.parser')

# Choisis une recette aléatoire parmis les 12 de la page et récupère des attributs de celle-ci
liste_recettes = soup.find_all('a', {'class':'MRTN__sc-1gofnyi-2 gACiYG'})
recette_aleatoire = liste_recettes[randint(0,11)]
recette = {
    'title': recette_aleatoire.find('h4', {'class':'MRTN__sc-30rwkm-0 dJvfhM'}).get_text(),
    'rate': recette_aleatoire.find('span', {'class':'SHRD__sc-10plygc-0 jHwZwD'}).get_text(),
    'url': marmiton + recette_aleatoire['href'],
    'ingredients': [],
    'etapes': []
}

# Aller dans la page de la recette sélectionnée grâce à l'url attribuée
recette_html = urllib.request.urlopen(recette['url']).read()
soup = BeautifulSoup(recette_html, 'html.parser')

# Ingrédients et étapes ajoutés dans les attributs de la recette en tableaux
for element in soup.find_all('span', {'class':'RCP__sc-8cqrvd-3 itCXhd'}):
    recette['ingredients'].append(element.get_text())
for element in soup.find_all('p', {'class':'RCP__sc-1wtzf9a-3 jFIVDw'}):
    recette['etapes'].append(element.get_text())

# Mise en forme de texte la note et les tableaux ingrédients et étapes pour l'envoi discord
ingredients_texte = "**Ingrédients :**"
for element in recette['ingredients']:
    ingredients_texte = ingredients_texte + "\n" + element.title()
etapes_texte = "**Etapes :**"
i = 1
for element in recette['etapes']:
    etapes_texte = etapes_texte + "\n" + str(i) + "- " + element
    i = i + 1
note_texte = "_Notée " + recette['rate'] + "_"

# Préparation et envoi du message discord sous forme d'embed avec les infos souhaitées
message_content = ingredients_texte + "\n\n" + etapes_texte + "\n\n" + note_texte
embed = [{
    "description": message_content,
    "title": recette["title"],
    "color": 1127128
}]
message = {
    "embeds": embed,
    "content": "Recette du jour !"
}
requests.post(webhook, json=message)