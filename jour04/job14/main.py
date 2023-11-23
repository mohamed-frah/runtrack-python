def my_long_word(longueur, phrase):
    """
    Retourne les mots d'une phrase qui sont plus longs qu'une longueur donnée.
    """
    words = phrase.split()  
    long_words = []  

    for word in words:
        if count_characters(word) > longueur:  
            long_words.append(word)

    return ' '.join(long_words)  

def count_characters(word):
    """
    Compte le nombre de caractères dans un mot sans utiliser la fonction len().
    """
    count = 0
    for caractere in word:
        count += 1
    return count

test_sentence = "Les poubelles des uns font les trésors des autres"
print(f"{my_long_word(3, test_sentence)}")