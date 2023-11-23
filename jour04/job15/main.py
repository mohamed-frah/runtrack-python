def custom_round(number):
    """
    Arrondit un nombre sans utiliser la fonction round().
    """
    integer_part = int(number)  
    decimal_part = number - integer_part  
    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

def custom_sort(list_to_sort):
   
    n = 0  
    for item in list_to_sort:
        n += 1

    
    for i in range(n):
        for j in range(0, n-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

    return list_to_sort


exemple_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

arrondi_et_trie = custom_sort([custom_round(num) for num in exemple_liste])
print (arrondi_et_trie)