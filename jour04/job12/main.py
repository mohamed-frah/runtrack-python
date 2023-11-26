liste = [4, 8, 75, 2, 15, 9, 7, 38, 6]    
def Gliste(liste):      
    n = 0               
    for chiffre in liste:              
        n += 1  
    i=0
    while i < n :
        j=0
        while j < (n-i-1):
            if liste[j] > liste[j+1]:
                liste[j],  liste[j+1] = liste[j+1], liste[j]
            j+=1                 
        i+=1      

    return liste

Gliste(liste)
print(Gliste(liste))

    
    
