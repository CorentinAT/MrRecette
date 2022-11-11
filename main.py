import requests
from marmiton import Marmiton
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

webhook = ""

# Search :
query_options = {
  "aqt": "tomates farcies",  # Query keywords - separated by a white space
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

for element in detailed_recipe["steps"]:
    etapes = etapes + element

msg = detailed_recipe["name"] + "\n**Ingrédients :**" + ingredients + "\n" + etapes

message = {
    "content" : msg
}

requests.post(webhook, json=message)
