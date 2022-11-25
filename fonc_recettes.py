class Recette:
    """

    """
    def __init__(self, nom, auteur=None, difficulte=None, temps=None, note=None, ingredients=[], etapes=[], lien=None):
        self.nom = nom
        self.auteur = auteur
        self.lien = lien
        self.note = note
        self.difficulte = difficulte
        self.temps = temps
        self.ingredients = ingredients
        self.etapes = etapes

    def __str__(self) -> str:
        texte = f"Recette : {self.nom}"
        if self.auteur:
            texte += f"\nAuteur : {self.auteur}"
        if self.difficulte:
            texte += f"\nDifficulté : {self.difficulte}"
        if self.temps:
            texte += f"\nDurée : {self.temps}"
        if self.note:
            texte += f"\nNote : {self.note}"
        if self.ingredients!=[]:
            texte += f"\nIngrédients :\n{self.str_ingr()}"
        if self.etapes!=[]:
            texte += f"\nEtapes :\n{self.str_etap()}"
        if self.lien:
            texte += f"\nLien : {self.lien}"
        return texte

    def str_ingr(self):
        """
        Met sous forme de texte la liste d'ingrédients (avec les quantités),
        Erreur si pas d'ingrédient associé
        """
        assert self.ingredients is not None, "Pas d'ingrédient associé à la recette"
        texte = ""
        for element in self.ingredients:
            ingr = element[0]
            ingr = ingr.title()
            try:
                ingr = f"{ingr} ({element[1]})"
            except:
                pass
            texte = texte + (f"{ingr}" if texte=="" else f"\n{ingr}")
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
        Ajouter ingrédient au tableau ingrédients de la recette.
        Arguments: (nom:str, quantité:str(facultatif)).
        Insere un sous tableau dans le tableau ingrédients.
        """
        if quantite:
            self.ingredients.append([nom, quantite])
        else:
            self.ingredients.append([nom])

    def ajouter_etape(self, etape, numero=None):
        """
        Ajouter une étape au tableau étapes de la recette.
        Arguments: (description:str, numero (falcultatif):int).
        Si pas de numéro d'étape ou numéro d'étape supérieur au nombre
        d'étapes existantes : mise en dernier.
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