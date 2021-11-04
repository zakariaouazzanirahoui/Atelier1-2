#Tri par Selection :
def tri_selection(tab):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

#Tri à bulle :
def tri_bulle(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]

#Tri par insertion :
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k


