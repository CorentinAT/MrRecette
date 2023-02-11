# MrRecette

MrRecette est un programme python qui envoie une recette aléatoire de marmiton sur un webhook discord.

## Status

Fini, à maintenir à jour pour les changements de classes sur le site de marmiton.

## Fonctionnement

Le projet contient 3 fichiers, un fichier **main.py** qui est le programme exécuté, qui s'occupe du choix aléatoire et de l'envoi sur discord.

Il utilise le module (dans le fichier **modules**) **marmiton.py**, qui utilise lui même le module **fonc_recettes.py**.

### Module fonc_recettes

Le module **fonc_recettes.py** contient une classe **Recette** qui permet de stocker et gérer des recettes avec ces attributs :

- Nom de la recette (**nom**) -> obligatoire
- Auteur de la recette (**auteur**)
- Lien vers la recette (**lien**)
- Difficulté de la recette (**difficulte**)
- Temps de préparation (**temps**)
- Liste des ingrédients (**ingredients**)
- Liste des étapes (**etapes**)

Les méthodes de cette classe sont les suivantes :

- Le print pour afficher la recette au global
- **str_ingr()** pour convertir la liste des ingrédients en chaîne de caracètere mise en forme
- **str_etap()** pour la même chose avec la liste d'étapes
- **ajouter_ingr()** pour ajouter un ingrédient, et eventuellement sa quantité
- **ajouter_etape()** pour ajouter une étape, et eventuellement son numéro

## Module marmiton

Le module **marmiton.py** contient une classe **Marmiton** et une fonction **recup_recette**.

La classe **Marmiton** permet de gérer les options de recherche d'une recette sur le site marmiton.
Toutes les options de recherche sont dans un seul attribut **options**  qui est un dictionnaire pouvant avoir les attributs suivants :

- Le nom ou les mots clés de la/les recette(s) cherchée(s) (**nom**)
- Le type de plat (entrée, dessert...), les différentes possibilités sont dans la déclaration de la méthode init (**type_plat**)
- La difficulté de la recette sous forme de numéro, les différentes possibilités sont dans la déclaration de la méthode init (**difficulte**)
- Le coût de la recette sous forme de numero, les différentes possibilités sont dans la déclaration de la méthode init (**cout**)
- Le temps de préparation sous forme de numero, les différentes possibilités sont dans la déclaration de la méthode init (**temps**)

Les méthodes de cette classe sont les suivantes :

- Un print pour afficher le dictionnaire **options** tel quel
- **recherche()** qui recherche sur marmiton les recettes en fonction des options associées à la classe, avec éventuellement le numéro de page que l'on souhaite, il renvoie un tableau de dictionnaire, qui contiennent chacun une fiche de recette contenant le lien, le nom et la note de la recette