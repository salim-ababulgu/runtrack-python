# Déclaration des variables des 'consoles' dans mon cas
nom_de_consoles = "switch"
prix_consoles = 500
quantite_en_stock_des_consoles = 900


# Affichage des informations du 'consoles' de manière formatée
print("Nom du produit :", nom_de_consoles, "de couleur noir")
print("Prix unitaire :", prix_consoles, "€")
print("Quantité en stock :", quantite_en_stock_des_consoles, "en stock")


# Ajout de nouveaux produits en stock
nouvelle_quantite = int(input("Entrez la quantité de produits à ajouter en stock : "))
quantite_en_stock_des_consoles += nouvelle_quantite

# Mise à jour du prix du produit suite à l'inflation
prix_consoles *= 1.1  # Augmentation de 10%

# Affichage des informations mises à jour sur le produit
print("\nAprès mise à jour :")
print("Nom du produit :", nom_de_consoles)
print("Prix unitaire :", prix_consoles, "€")
print("Quantité en stock :", quantite_en_stock_des_consoles)



