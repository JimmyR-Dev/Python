# ---------------------Les boucles----------------------------

# for est pour un nombre defini d'une action, while une boucle conditionnel, TANT QUE
# Si je veux faire passer tous les elements d'une liste
listePassagers = ["Jean Claude", "Gerard", "Stephane", "Didier"]
for passagers in listePassagers:
    print(passagers) # Tous les passagers de la liste seront afficher

print(f"il y'a {len(listePassagers)} personnes a bord")

# boucler un certain nombre de fois
for x in range(5):
    print(x) # Va boucler 5 fois de 0 a 4

for x in range(87, 90): # boucle sur la plage de 80 à 90
    print(f"{x} kinder bueno sur la table")