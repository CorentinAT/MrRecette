import requests
import os
from dotenv import load_dotenv
from random import randint
from modules.marmiton import Marmiton, recup_recette

# Remplacer ces deux lignes par "webhook = <lien du webhook>"
load_dotenv()
webhook = os.getenv("webhook")

options = Marmiton(type_plat='platprincipal', difficulte=1, cout=1, temps=45)
recherche = options.recherche(randint(1, 83))
recette = recup_recette(recherche[randint(0,11)]['lien'])

# Mise en forme de texte la note et les tableaux ingrédients et étapes pour l'envoi discord
ingredients_texte = "**Ingrédients :**\n" + recette.str_ingr()
etapes_texte = "**Etapes :**\n" + recette.str_etap()
note_texte = "_Notée " + recette.note + "_"

# Préparation et envoi du message discord sous forme d'embed avec les infos souhaitées
message_content = ingredients_texte + "\n\n" + etapes_texte + "\n\n" + note_texte
embed = [{
    "description": message_content,
    "title": recette.nom,
    "color": randint(0,16777215)
}]
message = {
    "embeds": embed,
    "content": "Recette du jour !"
}
requests.post(webhook, json=message)