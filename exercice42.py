set1={23,42,65,57,78,83,29}
set2={57,83,29,67,73,43,48}
#on utilise la fonction intersection 
set3=set1.intersection(set2)
#boucle for pour supprimer les elements d'intersection 
for valeur in set3:
    set1.remove(valeur)

print('intersection des deux sets donne :',set3)
print('set 1 apres supression :',set1)