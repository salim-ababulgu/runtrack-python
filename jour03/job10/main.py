# Créer une fonction qui vérifie que le nombre est pair ou impair
# Pensez à vérifier si le nombre est bien un chiffre entier et positif
# Depuis le programme, appelez cette fonction plusieurs fois avec des paramètres différents

def verifie(nombre):
    if type (nombre) != int or nombre < 0:
        print ("Veuillez entrez un nombre entier positif")
        return
    
    if nombre % 2 == 0:
        print("le", nombre, "est un nombre paire")
    else:
        print("le", nombre, "est un nombre impaire")

verifie(5)
verifie(15)
verifie(25)

















