
def sum(n):
    # critere de fin de boucle
    if n >= 1:   
        return n + sum( n - 1 )
    return n


n = int(input("saisir le nombre que vous voulez:"))
print("la somme est :",sum(n))

