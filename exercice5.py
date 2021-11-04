def nbrchiffres(nombre):
    # si le nombre est inferieur que 10 , son nbr de chiffre est 1
    if nombre < 10:
        return 1
    # si le nombre est superieur a 10, on le divise par 10 jusqu'il devient inferieur a 10
    else:
        return 1 + nbrchiffres(nombre / 10)


nombre = int(input("saisir le nombre :"))
print("le nombre de chiffre de", nombre, "est", nbrchiffres(nombre))