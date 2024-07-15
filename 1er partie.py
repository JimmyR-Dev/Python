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

# Verifier une liste avec leurs indices :
liste1 = ["facebook", "twitter", "instagram", "youtube"]
# les indices de type -3 etc prendses valeurs a l'envers, par exemple -1 est youtube
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
#
# index()
# Renvoie la première occurrence de l'élément spécifié dans la liste.
#
# count()
# Renvoie le nombre d'occurrences de l'élément spécifié dans la liste.
#
# reverse()
# Inverse l'ordre des éléments de la liste.


# Creer un Tuple permet d'obtenir le meme systeme que les listes (ou tableau) mais est immuable donc non modifiable.
# Exemple Tuple :
monTuple = ("France", "Allemagne", "Angleterre")
print(monTuple)
