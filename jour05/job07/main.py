def arondi(list):
    list_arondi = []
    for i in list:
        if i%5 >= 3:
            if i%5 == 3: 
                list_arondi += [i+2]
            elif i%5 == 4:
                list_arondi += [i+1]
        else:
            list_arondi += [i]
    return list_arondi

list = [85,84,83,82]
print(arondi(list))