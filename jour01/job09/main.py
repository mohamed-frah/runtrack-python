nom = "orange"
prix_unitaire  = 100
quantité_en_stock = 150
print(nom , prix_unitaire , quantité_en_stock)
nouveau_stock = quantité_en_stock + int(input("combien voulez-vous d'orange : " ))
print(nouveau_stock)
nouveau_prix = (prix_unitaire * 1.1 )
print(nouveau_prix)