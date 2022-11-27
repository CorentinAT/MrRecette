from modules.fonc_recettes import Recette
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import ssl

class Marmiton:
    """Class pour gérer de options de recherche et la recherche sur Marmiton"""
    def __init__(self, nom:str=None, type_plat:str=None, difficulte:int=None, cout:int=None, temps:int=None):
        """Prendre les filtres de recherche

        Args:
            nom (str, optional): mots-clé (barre de recherche). Defaults to None.
            type_plat (str, optional): entree, platprincipal, dessert, amusegueule, accompagnement, sauce, boisson ou confiserie. Defaults to None.
            difficulte (int, optional): 1->Très facile, 2->Facile, 3->Moyen, 4->Difficile. Defaults to None.
            cout (int, optional): 1->Bon marché, 2->Coût moyen, 3->Assez cher. Defaults to None.
            temps (int, optional): 15->Moins de 15min, 30->Moins de 30min, 45->Moins de 45min. Defaults to None.
        """
        options = dict()
        if nom:
            options['aqt'] = nom
        if type_plat:
            options['dt'] = type_plat
        if difficulte:
            options['dif'] = difficulte
        if cout:
            options['exp'] = cout
        if temps:
            options['ttlt'] = temps
        self.options = options

    def __str__(self)->str:
        """Inititalisation du print(Marmiton)

        Returns:
            str: Chaine qui va être print lors de l'appel de celui-ci
        """
        return str(self.options)

    def recherche(self, page:int=None)->list:
        """Recherche une page de recettes selon les paramètres de la class

        Args:
            page (int, optional): Le numéro de page qui va être recherché. Defaults to None.

        Raises:
            ValueError: Erreur si le numéro de page donné est trop haut

        Returns:
            list: Liste des noms, notes et liens des recettes de la page
        """
        ssl._create_default_https_context = ssl._create_unverified_context
        options_recherche = self.options
        if page and page>1:
            options_recherche['page'] = page
        options_url = urllib.parse.urlencode(options_recherche)
        recherche_url = "https://www.marmiton.org/recettes/recherche.aspx?" + options_url
        try:
            resultat_html = urllib.request.urlopen(recherche_url).read()
            soup = BeautifulSoup(resultat_html, 'html.parser')
        except:
            raise ValueError("Cette page n'existe pas, essayez un nombre plus bas")
        resultats = []
        liste_fiches = soup.find_all('a', {'class':'MRTN__sc-1gofnyi-2 gACiYG'})
        for element in liste_fiches:
            fiche = dict()
            fiche['nom'] = element.find('h4', {'class':'MRTN__sc-30rwkm-0 dJvfhM'}).get_text()
            fiche['note'] = element.find('span', {'class':'SHRD__sc-10plygc-0 jHwZwD'}).get_text()
            fiche['lien'] = 'https://www.marmiton.org' + element['href']
            resultats.append(fiche)
        return resultats

def recup_recette(url:str)->classmethod(Recette):
    """Récupère toutes les informations d'une recette depuis son url

    Args:
        url (str): Lien de la recette souhaitée (peut être récupéré depuis Marmiton.recherche())

    Returns:
        class Recette: Class du module fonc_recettes.py qui contient toutes les informations de la recette
    """
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    recette = Recette(soup.find('h1', {'class':'SHRD__sc-10plygc-0 itJBWW'}).get_text())
    recette.lien = url
    recette.auteur = soup.find('div', {'class':'RCP__sc-ox3jb6-5 fwQMuu'}).get_text()
    temps_diff = soup.find_all('p', {'class':'RCP__sc-1qnswg8-1 iDYkZP'})
    recette.temps = temps_diff[0].get_text()
    recette.difficulte = temps_diff[1].get_text()
    recette.note = soup.find('span', {'class':'SHRD__sc-10plygc-0 jHwZwD'}).get_text()
    liste_ingredients = soup.find_all('div', {'class':'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-3 MuiGrid-grid-sm-3'})
    for element in liste_ingredients:
        try:
            ingr = element.find('span', {'class':'RCP__sc-8cqrvd-3 cDbUWZ'}).get_text()
        except:
            ingr = element.find('span', {'class':'RCP__sc-8cqrvd-3 itCXhd'}).get_text()
        try:
            qt = element.find('span', {'class':'SHRD__sc-10plygc-0 epviYI'}).get_text()
            if qt==" " or qt=="":
                raise ValueError()
            recette.ajouter_ingr(ingr, qt)
        except:
            recette.ajouter_ingr(ingr)
    liste_etapes = soup.find_all('p', {'class':'RCP__sc-1wtzf9a-3 jFIVDw'})
    for element in liste_etapes:
        recette.ajouter_etape(element.get_text())
    return recette