# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Affichage du gain annuel en fonction du taux de rendement
gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print("Gain annuel initial :", gain_annuel, "euros")

# L'investisseur augmente son capital de 5 000 euros
montant_initial += 5000
# Le taux augmente alors de 2%
taux_rendement_annuel += 2

# Calcul du nouveau gain de l'investisseur
nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print("Nouveau gain annuel :", nouveau_gain_annuel, "euros")

# L'investisseur retire 10% du montant total
montant_initial -= montant_initial * 0.10
# Suite à ce retrait, le rendement diminue de 1%
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement
montant_final = montant_initial + nouveau_gain_annuel
print("Montant final de l'investissement :", montant_final, "euros")
