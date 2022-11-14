import requests
from marmiton import Marmiton
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

webhook = "https://discord.com/api/webhooks/1041675147481985026/4qr1pUQdSkd6nvYaUjVMimLK-SJB6rLfYGNWGDQhrYoRAUHcHzySsaD7XPAffG0LyTyG"

# Search :
query_options = {
  "aqt": "pates",  # Query keywords - separated by a white space
  "dt": "platprincipal",       # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optional)
  "exp": 2,                    # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
  "dif": 2,                    # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
  "veg": 0,                    # Vegetarien only : 0 -> False, 1 -> True (optional)
}
query_result = Marmiton.search(query_options)

# Get :
recipe = query_result[0]
recipe_url = recipe["url"]
detailed_recipe = Marmiton.get(recipe_url)

ingredients = ""
for element in detailed_recipe["ingredients"]:
    ingredients = ingredients + "\n" + element

etapes = ""
i = 1

for element in detailed_recipe["steps"]:
    etapes = etapes + "\n" + str(i) + "- " + element
    i = i + 1

msg = detailed_recipe["name"] + "\n**Ingrédients :**" + ingredients + "\n" + etapes

message = {
    "content" : msg
}

requests.post(webhook, json=message)
