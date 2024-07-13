maVariable1 = 10
maVariable2 = 20
maVariable3 = maVariable1 + maVariable2
print(maVariable3)

# Ici, j'utilise une F-string qui permet d'utiliser plusieurs variables dans une chaine de charactere
print(f"Ce matin j'ai eu {maVariable1} gateaux et j'ai pu avoir {maVariable3} boissons !")

# Une autre manière de faire, ici, je ne peux pas directement mettre une variable qui contient une valeur de chiffre
# si je veux le faire, je dois convertire en string avec str
string1 = "Fraises"
string2 = 32
print("Ce matin, j'ai eu des " + string1 + " pourtant j'ai " + str(string2) + "ans")
