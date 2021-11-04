#fonction recursive de fibonacci
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))



n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
#boucle for pour utiliser la fonction de fibonacci
for i in range(n):
    print(fibonacci(i))