# -------------------------Les conditions--------------------------

# Une condition en python s'écrit
ensoleiller = True
pluie = False

if ensoleiller:
    print("il fait beau aujourd'hui")
elif pluie: # autant de conditions que necessaire
    print("il pleut aujourd'hui")
else:
    print("quel temps fait il aujourd'hui ?")

# Coupler des conditions, je peux utiliser avec if : and, or, ou not(si c'est faux)

# exemple 1
# si ensoleiller et pluie sont vrais alors la 1ere instruction s'applique, sinon la 2eme
if ensoleiller and pluie:
    print("Les deux variables sont vraies")
else:
    print("Erreur, ne remplie pas toutes les conditions")

# exemple 2
if ensoleiller and not pluie:
    print("ensoleiller est vrai, pluie est faux")
else:
    print("erreur, ne remplie pas toutes les conditions")

# Operateurs (les operateurs sont les memes que javascript)

sandwichs = 10
kebabs = 25

# On prend ce qu'on a en plus, si on a plus de sandwichs ou egal on prend les sandwichs, sinon les on prend les kebabs
# Si c'est egal, on prend tout
if sandwichs != kebabs:
    print("on prend les sandwichs")
elif sandwichs == kebabs:
    print("on prend les deux")
else:
    print("on prend les kebabs")

# Les matchs cases

# j'utilise une condition en cascade, qui s'arrete si la valeur est vraie
transports = "train"
match transports:
    case "voiture":
        print("Je prend la voiture car je gagne du temps")
    case "bus":
        print("Je prend le bus car c'est moins cher")
    case "train":
        print("Je prend le train car c'est plus respectueux de l'environnement")
    case _: # si rien est vrai
        print("Je pars à pieds")

# exercice
nombre_a_gauche = 20
nombre_a_droite = 10
symbole = "/"
resultat = 0

if isinstance(nombre_a_gauche, int) and isinstance(nombre_a_droite, int):
    print("Les nombres de gauche et droite sont bien des entier")
else:
    print("erreur, ceci n'est pas un entier")
    exit() # sort du programme et s'arrette ici si la condition est remplie

match symbole:
    case "+":
        resultat = nombre_a_gauche + nombre_a_droite
    case "-":
        resultat = nombre_a_gauche - nombre_a_droite
    case "*":
        resultat = nombre_a_gauche * nombre_a_droite
    case "/":
        if nombre_a_droite == 0:
            print("erreur, ne peux etre divisé par 0")
            exit()
        resultat = nombre_a_gauche / nombre_a_droite # utiliser // si je veux l'entier et pas les dicimale en resultat
    case _:
        print("erreur, aucun operateur ne correspond")
        exit()

print(f"le resultat est de : {resultat}")