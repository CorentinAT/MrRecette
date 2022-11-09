import requests
from marmiton import Marmiton
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

webhook = "https://discord.com/api/webhooks/1039873910302310463/5dRCWhSTc4snYlHGL4twNhWEUQcrb2tUOTMXFwvcKbppwzdpZaG6afDVfy_dGs_7V-Jm"

# Search :
query_options = {
  "aqt": "boeuf bourguignon",  # Query keywords - separated by a white space
}
query_result = Marmiton.search(query_options)

print(query_result)

# Get :
recipe = query_result[0]
main_recipe_url = recipe['url']

try:
    detailed_recipe = Marmiton.get(main_recipe_url)  # Get the details of the first returned recipe (most relevant in our case)
except RecipeNotFound as e:
    print(f"No recipe found for '{query_options['aqt']}'")
    import sys
    sys.exit(0)


message = {
    "content" : detailed_recipe['name']
}

requests.post(webhook, json=message)