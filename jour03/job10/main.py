def pair_impair(chiffre):
    if chiffre >0 and type(chiffre) == int:
        if chiffre % 2 == 0:
            print("pair")
        elif chiffre % 2 != 0:
            print("impair")
    else:
        print("votre chiffre ne serre a rien")

pair_impair(-1001)
