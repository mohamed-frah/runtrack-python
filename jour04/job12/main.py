liste = [4, 8, 5, 2, 1, 9, 7, 3, 6]    
def Gliste(liste):      
    n = 0               
    for chiffre in liste:              
        n += 1                         

    for i in range(n):              
        for j in range(0, n-i-1):       
            if liste[j] > liste[j+1]:        
                liste[j], liste[j+1] = liste[j+1], liste[j]        

    return liste

Gliste(liste)
print(Gliste(liste))

    
    
