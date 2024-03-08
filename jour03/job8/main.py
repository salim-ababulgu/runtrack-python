# Créer une fonction qui prend 2 paramètres :
# --> Le premier reçoit un String nommé « type »
# --> Le second reçoit un String nommé « saison »
    # Si la valeur de « type » est égale à « fruits » et que celle de saison est égale à «..
        # ..hiver », affichez « orange, mandarine et kiwi »
    # Si la valeur de « type » est égale à « fruits » et que celle de saison est égale à «..
        # ..été », affichez « Poire, fraise, cassis »
    # Si la valeur de « type » est égale à « légume » et que celle de saison est égale..
        # ..à « hiver », affichez « carotte, topinambour, endive »
    # Si la valeur de « type » est égale à « légume » et que celle de saison est égale..
        # ..à « été », affichez « artichaut, aubergine,navet »


def lorem(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "fruit" and saison == "hiver":
        print("tu es un développeur logiciel")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine,navet")
    else:
        print("")

lorem("fruit", "hiver")