LIST=[11,45,8,11,23,45,23,45,89]
#on crée un dictionnaire
dict={}
for valeur in LIST :
    # on teste si le nombre a des occurences ,si non on retourn 1 
    #Pour récupérer les valeurs on utilise la méthode keys .
    if valeur not in dict.keys() :
        dict[valeur]=1
    #si oui on incremente la valeure de 1
    else: 
            dict[valeur]=dict[valeur] + 1
print("la list de depart :",LIST)
print("la nouvelle liste en comptant les occurences :",dict)