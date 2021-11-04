def inverse(str):
    # creation d'une chaine de caractere vide
    new_str = ""
    if str != "":
        #on donne a la nouvelle chaine le dernier caractere a chaque fois 
        new_str = inverse(str[1:]) + str[0]
        # resultat= une chaine inversé
    return new_str

str = str(input("saisir la chaine de caractere:"))
print("la chaine inversé est :", inverse(str))
