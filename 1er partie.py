maVariable1 = 10
maVariable2 = 20
maVariable3 = maVariable1 + maVariable2
print(maVariable3)

# Ici, j'utilise une F-string qui permet d'utiliser plusieurs variables dans une chaine de charactere
# Ici, pas besoin de str, il le reconnait un chiffre dans une variable
print(f"Ce matin j'ai eu {maVariable1} gateaux et j'ai pu avoir {maVariable3} boissons !")

# Une autre manière de faire, ici, je ne peux pas directement mettre une variable qui contient une valeur de chiffre
# si je veux le faire, je dois convertire en string avec str
string1 = "Fraises"
string2 = 32
print("Ce matin, j'ai eu des " + string1 + " pourtant j'ai " + str(string2) + "ans")

booleen1 = True
booleen2 = False
# Permet de verifier de quel type est la valeur d'une variable
print(f"Cette variable est de type : {type(booleen1)}")

# ---------------------------LISTES ET TABLEAUX---------------------------------------
# Verifier une liste avec leurs indices :
liste1 = ["facebook", "twitter", "instagram", "youtube"]
# les indices de type -3 etc prennent ses valeurs à l'envers, par exemple -1 est youtube
print(liste1[-3])

# Dans une chaine de caractere, le [2] va renoyer T, je peux faire la meme chose avec les lettres ici.
langage = "PYTHON"
print(langage[2])

# Va remplacer twitter par LinkdIn, en utilisant son indice et en remplacant la valeur.
liste2 = ["facebook", "twitter", "instagram", "youtube"]
liste2[1] = "LinkdIn"
print(liste2)

# ajoute TikTok a la liste en dernier, et supprime twitter
liste3 = ["daylimotion", "twitter", "instagram", "youtube"]
liste3.append("TikTok")
liste3.remove("twitter")
print(liste3)

# connaitre la longueur de la liste
print(len(liste3))

# extend()
# Ajoute plusieurs éléments à la fin de la liste.

# insert()
# Insère un élément à une position donnée dans la liste.
#
# pop()
# Supprime et renvoie l'élément à une position donnée de la liste, ou le dernier élément si aucun indice n'est spécifié.
# Et se base sur l'index, contrairement à remove qui se base sur la valeur
# index()
# Renvoie la première occurrence de l'élément spécifié dans la liste.
#
# count()
# Renvoie le nombre d'occurrences de l'élément spécifié dans la liste.
#
# reverse()
# Inverse l'ordre des éléments de la liste.
#
# sort()
# Trie les elements du tableau par ordre alphabetique

# Creer un Tuple permet d'obtenir le meme systeme que les listes (ou tableau) mais est immuable donc non modifiable.
# Exemple Tuple :
monTuple = ("France", "Allemagne", "Angleterre")
print(monTuple)

# Par contre, je peux concaténer deux Tuples

premierTuple = (1, 2, 3)
deuxiemeTuple = ("premier", "deuxieme", "troisieme")
nouveauTuple = premierTuple + deuxiemeTuple
print(nouveauTuple)
# Pour trouver si un élément est dans une liste ou un Tuple, renvois true ou false si présent ou non.
print(2 in premierTuple)
print(4 in premierTuple)

# ----------------------------Dictionnaire Cle : Valeur--------------------

# Deux manières de faire :
# Je peux utiliser un systeme de cle : valeur, ici, j'initialise campagne de type dictionnaire
campagne = {}
# J'utilise plusieurs clés avec leurs valeurs
campagne["nom"] = "les chiens sont les meilleurs animaux"
campagne["maison"] = "Les maisons en bord de mer sont les meilleurs"
print(campagne["nom"])
print(campagne["maison"])

# Ou, j'initialise une variable en tant que dictionnaire et je renseigne mes paires cles/valeurs directement

infoCampagne = {
    "nom": "Coluche",
    "age": "47",
    "nom de partie": "Les gigolos",
    "date de debut": "27/07/2024",
    "influenceurs": ["@Deccyptique", "@Argon"]
}

print(infoCampagne["nom"]) # affiche Coluche

# Ajoute une paire cle valeur à la suite de identite
identite = {
    "nationalite": "france",
    "origine": "portugal"
}

identite["animal"] = "chien"
print(identite)

# remplace la valeur de nationalite par espagne
identite["nationalite"] = "espagne"
print(identite)

# supprime une paire cle valeur
del identite["origine"]
print(identite)
# ou
identite.pop("nationalite")
print(identite)

# Si je veux trouver une cle en particulier, je peux proceder comme suit, et cela me renvoie true ou false
print("animal" in identite)

# LISTE D' AUTRES METHODES
# keys()
# Retourne une vue sur les clés du dictionnaire.
# nom_du_dictionnaire.keys()
#
# values()
# Retourne une vue sur les valeurs du dictionnaire.
#  nom_du_dictionnaire.values()
#
# items()
# Retourne une vue sur les couples (clé, valeur) du dictionnaire.
#  nom_du_dictionnaire.items()
#
# get(clé)
# Retourne la valeur associée à la clé spécifiée. Si la clé n'est pas présente dans le dictionnaire, retourne la valeur None.
#  nom_du_dictionnaire.get(clés)
#
# pop(clé)
# Supprime la clé spécifiée et retourne la valeur associée. Si la clé n'est pas présente dans le dictionnaire, retourne la valeur None.
#  nom_du_dictionnaire.pop(clés)
#
# clear()
# Supprime tous les éléments du dictionnaire.
#  nom_du_dictionnaire.clear()
