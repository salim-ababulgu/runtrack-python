# Créez une fonction qui prend en paramètre une String nommée « langage »
    # Si la valeur de « langage » est égale à « JavaScript » ..
        # ..affichez : « tu es un développeur web »
    # Sinon si la valeur de « langage » est égale à « python » ..
        # ..affichez : « tu es un développeur web »
    # Sinon si la valeur de « langage » est égale à « java » ..
        # ..affichez : « tu es un développeur logiciel »
    # Sinon si la valeur de « langage » est égale à « reactjs » ..
        # ..affichez : « tu es un développeur mobile »
    # Sinon, affichez : « un jour, je serai le meilleur développeur... »


def dev(langage):
    if langage == "javascript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur web")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur développeur...")

dev("javascript")