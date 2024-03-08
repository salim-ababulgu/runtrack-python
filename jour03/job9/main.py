# Créez une fonction nommée « moyenne »
# qui prend en paramètre 3 notes et retourne la moyenne de ces notes
# Demandez à l'utilisateur de saisir trois notes
# puis enregistrez le résultat de la fonction « moyenne » ..
    # ..dans une variable appelée « moyenne_etudiant »


# Afficher ensuite la phrase suivante en fonction de la moyenne de l’étudiant :
# --> Très bon élève si la moyenne est comprise entre 20 et 15
# --> Bon élève si la moyenne est comprise entre 14 et 11
# --> Élève moyen si la moyenne est comprise entre 10 et 8
# --> Élève devant faire des efforts si la moyenne est comprise entre 0 et 7




def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("Entrez la note 1 : "))
note2 = float(input("Entrez la note 2 : "))
note3 = float(input("Entrez la note 3 : "))


moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
    print("Trèq bon élève 🎓")
if moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
    print("Bon élève 😃")
if moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
    print("Élève moyen 😐")
if moyenne_etudiant >= 7 and moyenne_etudiant <= 0:
    print("Élève devant faire des efforts 😞")


print(moyenne_etudiant)
