# options à faire :
# creation de recette
# passage sous forme de texte
# faire une recherche (avec toutes les options)
# prendre une page (choisie ou aleatoire)
# prendre une recette sur la page (choisie ou aleatoire)
# afficher les differentes parties de la recette (ingredients, auteur, etapes...)

class Ingredient:
    """

    """
    def __init__(self, nom:str, quantite:str):
        self.nom = nom
        self.quantite = quantite
    
    def __str__(self) -> str:
        return f"{self.nom} : {self.quantite}"

class Recette:

    etapes = []

    """

    """
    def __init__(self, nom=None, ingredients=[], etapes=[], auteur=None, lien=None, temps=None, difficulte=None, note=None):
        self.nom = nom
        self.auteur = auteur
        self.lien = lien
        self.note = note
        self.difficulte = difficulte
        self.temps = temps
        self.ingredients = ingredients
        self.etapes = etapes

    def __str__(self) -> str:
        return f""

    def str_ingr(self):
        """
        Met sous forme de texte la liste d'ingrédients (avec les quantités),
        Erreur si pas d'ingrédient associé
        """
        assert self.ingredients is not None, "Pas d'ingrédient associé à la recette"
        texte = ""
        for element in self.ingredients:
            texte = texte + (element if texte=="" else f"\n{element}")
        return texte

    def str_etap(self):
        """
        Met sous forme de texte les étapes,
        Erreur si pas d'étape associée
        """
        assert self.etapes is not None, "Pas d'étape associée à la recette"
        texte = ""
        i = 1
        for element in self.etapes:
            texte = texte + ("" if texte=="" else "\n") + f"{i}- {element}"
            i += 1
        return texte

    def ajouter_ingr(self, nom:str, quantite=None):
        """

        """
        if quantite:
            self.ingredients.append([nom, quantite])
        else:
            self.ingredients.append([nom])

    def ajouter_etape(self, etape, numero=None):
        """
        
        """
        assert numero!=0, "L'étape 0 ne peut pas exister"
        if not numero or numero-1>len(self.etapes):
            self.etapes.append(etape)
        else:
            l = len(self.etapes) - 1
            self.etapes.append("")
            while l>=numero-1:
                self.etapes[l+1] = self.etapes[l]
                l -= 1
            self.etapes[numero-1] = etape