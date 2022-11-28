class Recette:
    """Gérer, afficher et modifier des recettes"""
    def __init__(self, nom:str, auteur:str=None, difficulte:str=None, temps:str=None, note:str=None, ingredients:list=[], etapes:list=[], lien:str=None):
        """Tous les attributs de la recette

        Args:
            nom (str): Nom du plat
            auteur (str, optional): Auteur de la recette. Defaults to None.
            difficulte (str, optional): Difficulté de la recette. Defaults to None.
            temps (str, optional): Temps de préparation. Defaults to None.
            note (str, optional): Note de la recette (par ex récupéré sur un site). Defaults to None.
            ingredients (list, optional): Liste de sous-listes du format ["nom de l'ingrédient","quantité"(quantité optionnelle)]. Defaults to [].
            etapes (list, optional): Liste des étapes de la préparation. Defaults to [].
            lien (str, optional): Lien vers la recette. Defaults to None.
        """
        self.nom = nom
        self.auteur = auteur
        self.lien = lien
        self.note = note
        self.difficulte = difficulte
        self.temps = temps
        self.ingredients = ingredients
        self.etapes = etapes

    def __str__(self)->str:
        """Pour print(Recette), en fonction des attributs de la recette existants

        Returns:
            str: texte qui va être affiché à l'appel du print
        """
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

    def str_ingr(self)->str:
        """Mise en forme de texte la liste d'ingrédients, erreur si pas d'ingrédient

        Returns:
            str: Sous la forme: <ingrédient> (<quantité(s'il y a)>) <saut de ligne>...
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

    def str_etap(self)->None:
        """Mise en forme de texte la liste d'étapes, erreur si pas d'étape

        Returns:
            _type_: Sous la forme: <numéro d'étape>- <étape> <saut de ligne>...
        """
        assert self.etapes is not None, "Pas d'étape associée à la recette"
        texte = ""
        i = 1
        for element in self.etapes:
            texte = texte + ("" if texte=="" else "\n") + f"{i}- {element}"
            i += 1
        return texte

    def ajouter_ingr(self, nom:str, quantite:str=None)->None:
        """Ajoute un ingrédient donné aux attributs de la recette, sous la forme [ingr, quantité(optionnel)]

        Args:
            nom (str): Nom de l'ingrédient
            quantite (str, optional): Quantité de l'ingrédient, ex: "25 cl". Defaults to None.
        """
        if quantite:
            self.ingredients.append([nom, quantite])
        else:
            self.ingredients.append([nom])

    def ajouter_etape(self, etape:str, numero:int=None)->None:
        """Ajoute une étape aux attributs de la recette

        Args:
            etape (str): Description de l'étape
            numero (int, optional): Place où l'étape sera placée dans la liste d'étapes, erreur si numéro trop bas. Defaults to None.
        """
        assert not numero or numero>0, "L'étape 0 ou moins ne peut pas exister"
        if not numero or numero-1>len(self.etapes):
            self.etapes.append(etape)
        else:
            l = len(self.etapes) - 1
            self.etapes.append("")
            while l>=numero-1:
                self.etapes[l+1] = self.etapes[l]
                l -= 1
            self.etapes[numero-1] = etape