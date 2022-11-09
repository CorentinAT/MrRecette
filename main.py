import requests
from marmiton import Marmiton, RecipeNotFound

webhook = "https://discord.com/api/webhooks/1039873910302310463/5dRCWhSTc4snYlHGL4twNhWEUQcrb2tUOTMXFwvcKbppwzdpZaG6afDVfy_dGs_7V-Jm"

query_options = {
  "aqt": "boeuf bourguignon",  # Query keywords - separated by a white space
  "dt": "platprincipal",       # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optional)
  "exp": 2,                    # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
  "dif": 2,                    # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
  "veg": 0,                    # Vegetarien only : 0 -> False, 1 -> True (optional)
}

query_result = Marmiton.search(query_options)

recipe = query_result[0]
main_recipe_url = recipe["url"]

try:
    detailed_recipe = Marmiton.get(main_recipe_url)  # Get the details of the first returned recipe (most relevant in our case)
except RecipeNotFound as e:
    print(f"No recipe found for '{query_options['aqt']}'")
    import sys
    sys.exit(0)

message = {
    "content" : recette
}

requests.post(webhook, json=message)