#Fonction factoriel en utilisant la recursivit√© 
def factoriel(nombre):
    if nombre == 0 or nombre == 1 :
        return 1 
    return nombre * factoriel(nombre-1) 

#calcul de la somme de la serie de 1 a 5
u=0
s=0
for i in range(1,7):
        s = s + u
        u = factoriel(i) / i
print("la somme de la serie est :",s) 