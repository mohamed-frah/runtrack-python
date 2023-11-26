def remove_doublons(input_list):
    print(f"Liste avant suppression des doublons : {liste}")
    unique_liste = [] 
    for chiffre in input_list:
        if chiffre not in unique_liste:
            unique_liste.append(chiffre)
    return unique_liste

liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(f"Liste après suppression des doublons : {remove_doublons(liste)}")
