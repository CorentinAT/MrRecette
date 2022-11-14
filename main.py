import requests
from marmiton import Marmiton #module modifié pour que les class correspondent aux mises à jour du site
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

webhook = os.getenv("webhook")

# Search :
query_options = {
  "aqt": "gratin dauphinois",  # Query keywords - separated by a white space
  "dt": "platprincipal",       # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optional)
  "exp": 1,                    # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
  "dif": 1,                    # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
  "veg": 0,                    # Vegetarien only : 0 -> False, 1 -> True (optional)
}
query_result = Marmiton.search(query_options)

# Get :
recipe = query_result[0]
recipe_url = recipe["url"]
detailed_recipe = Marmiton.get(recipe_url)

ingredients = ""
for element in detailed_recipe["ingredients"]:
    ingredients = ingredients + "\n- " + element.title()

etapes = ""
i = 1

for element in detailed_recipe["steps"]:
    etapes = etapes + "\n" + str(i) + "- " + element
    i = i + 1

msg = "**Ingrédients :**" + ingredients + "\n\n**Etapes :**" + etapes

embed = [{
    "description": msg,
    "title": detailed_recipe["name"]
}]

message = {
    "embeds" : embed
}

requests.post(webhook, json=message)