def decimal_to_binary(nombre):
    # on crée une chaine vide
    binary=""
    while nombre != 0 :
        binary += str(nombre % 2)
        nombre = nombre // 2
        # on ajoute le dernier element a la chaine de caractere
    return binary[::-1]


nombre = int(input("saisir le nombre :"))
print("le nombre binaire est :", decimal_to_binary(nombre))


