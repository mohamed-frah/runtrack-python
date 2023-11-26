def my_long_word(longueur, phrase):
   
    words = phrase.split()  
    long_words = []  

    for word in words:
        if count_characters(word) > longueur:  
            long_words.append(word)

    return ' '.join(long_words)  

def count_characters(word):
  
    count = 0
    for caractere in word:
        count += 1
    return count

test_sentence = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(f"{my_long_word(3, test_sentence)}")