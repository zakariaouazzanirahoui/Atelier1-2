liste = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {'yassine': 47, 'imane': 69, 'mohamed': 76, 'abir': 97}

nvliste = []
for val in liste:
    if val in dict.values():
        nvliste.append(val)

print("liste :",liste)
print("dict :",dict)


print("liste contient que les valeurs de clé :",nvliste)
