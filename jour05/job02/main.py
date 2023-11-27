def rectangle(width, height):
    hauteur = '|' + '-' * (width-2) + '|'
    print(hauteur)

    for _ in range(height - 2):
        largeur = '|' + ' ' * (width - 2) + '|'
        print(largeur)

    if height > 1 :
        print(hauteur)

rectangle(10, 3)