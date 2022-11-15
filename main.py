import requests
import ssl
import os
import urllib
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from random import randint

load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

webhook = os.getenv("webhook")
marmiton = "https://www.marmiton.org"
marmiton_recherche = "https://www.marmiton.org/recettes/recherche.aspx?"

# Search :
options = {
  "dt": "platprincipal",       # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optional)
  "exp": 1,                    # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
  "dif": 1,                    # Vegetarien only : 0 -> False, 1 -> True (optional)
  "ttlt":45                    # Maximum preparation time : 15 -> -15min, 30 -> -30min, 45 -> -45min (optional)
}

options_url = urllib.parse.urlencode(options)
recherche_url = marmiton_recherche + options_url
resultat_html = urllib.request.urlopen(recherche_url).read()

soup = BeautifulSoup(resultat_html, 'html.parser')

pages = soup.find_all('a', {'class':'SHRD__sc-1ymbfjb-1 MTkAM'})

no_page_aleatoire = randint(0,17)

if no_page_aleatoire!=1:
    page_url = marmiton + pages[no_page_aleatoire]['href']
    resultat_html = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(resultat_html, 'html.parser')

liste_recettes = soup.find_all('a', {'class':'MRTN__sc-1gofnyi-2 gACiYG'})

recette_aleatoire = liste_recettes[randint(0,11)]

recette = {
    'title': recette_aleatoire.find('h4', {'class':'MRTN__sc-30rwkm-0 dJvfhM'}).get_text(),
    'rate': recette_aleatoire.find('span', {'class':'SHRD__sc-10plygc-0 jHwZwD'}).get_text(),
    'url': marmiton + recette_aleatoire['href'],
    'ingredients': [],
    'etapes': []
}

# print(recette['url'])
# print(recette['name'])
# print(recette['rate'])

recette_html = urllib.request.urlopen(recette['url']).read()
soup = BeautifulSoup(recette_html, 'html.parser')

for element in soup.find_all('span', {'class':'RCP__sc-8cqrvd-3 itCXhd'}):
    recette['ingredients'].append(element.get_text())

for element in soup.find_all('p', {'class':'RCP__sc-1wtzf9a-3 jFIVDw'}):
    recette['etapes'].append(element.get_text())

ingredients_texte = "**Ingrédients :**"
for element in recette['ingredients']:
    ingredients_texte = ingredients_texte + "\n" + element.title()

etapes_texte = "**Etapes :**"
i = 1
for element in recette['etapes']:
    etapes_texte = etapes_texte + "\n" + str(i) + "- " + element
    i = i + 1

message_content = ingredients_texte + "\n\n" + etapes_texte

embed = [{
    "description": message_content,
    "title": recette["title"],
    "color": 1127128
}]

message = {
    "embeds" : embed
}

requests.post(webhook, json=message)