# Je créer une fonction "L"
# Je créer une liste d'entier(chiffres) " ["1", "2", "3", "4", "5"] "


# Création de la liste L
L = [1, 2, 3, 4, 5]

# -> Affichage de la deuxième valeur de la liste
print(L[1])

# -> Fonction pour remplacer L[3] par la somme des cases voisines
def remplacer_valeur(liste):
  liste[3] = liste[2] + liste[4]

# Appel de la fonction
remplacer_valeur(L)

# Affichage de la liste après modification
print(L)

# -> Affichage de la dernière valeur de la liste
print(L[-1])




