# Créer une fonction nommée « time_to_text »
#  Qui prend en paramètre un « nombre entier » de minutes
# Et « affiche en console » une chaine de caractère..
    # ..sous la forme de : « X heures et Y minutes ».
#   Exemples:  2heures et 40 minutes


def time_to_text(minutes):
    # Calcul du nombre d'heures
    heures = minutes // 60
    # Calcul du nombre de minutes restantes
    minutes_restantes = minutes % 60
    # Affichage dans le format demandé
    print(f"{heures} H {minutes_restantes} minutes")

# Exemple d'utilisation
time_to_text(165)  # Affichera "2 H 45 minutes"



