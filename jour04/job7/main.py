# Écrire un programme qui compte le nombre de multiples... 
# ...de 3 présents dans la liste : L = [8, 24,48,2,16].
# ------------------------------------------------ #

L = [8, 24, 48, 2, 16]
nb_multiples_3 = 0

# Parcourir la liste
for nombre in L:
  # Tester si le nombre est divisible par 3
  if nombre % 3 == 0:
    # Incrémenter le compteur si c'est le cas
    nb_multiples_3 += 1

# Afficher le résultat
print(f"Nombre de multiples de 3 : {nb_multiples_3}")




