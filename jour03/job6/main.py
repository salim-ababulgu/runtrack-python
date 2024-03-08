# Créer une fonction qui prend en paramètre un nombre nommé « nombre »
# Afficher « positif » si le nombre est supérieur à 0
# Afficher « négatif » si le nombre est inférieur à 0
# Depuis le programme, appelez cette fonction plusieurs fois avec des paramètres différents


def calcule(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("😐")

# Appels de la fonction avec différents paramètres
calcule(5)
calcule(-2)
calcule(0)
