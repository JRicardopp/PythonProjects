import os
import random


def data_out(filepath="ahorcado/data.txt"):
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace("\n", " ")
            data.append(line.strip(). upper())
    return data 


def run():
    word = data_out(filepath='ahorcado/data.txt')
    random_word =  random.choice(word)
    n_data = random_word.maketrans("ÁÉÍÓÚ", "AEIOU")
    random_word_n = random_word.translate(n_data)
    random_word_list = [letter for letter in random_word_n]
    random_word_underscort = ["_"] * len(random_word_list)
    letter_index = {}
    for idx, letter in enumerate(random_word_n):
        if not letter_index.get(letter):
            letter_index[letter] = []
            letter_index[letter].append(idx)
        print(letter_index)
    while True:
        os.system('clear')
        
        print("¡Adivina la palabra!")
        for element in random_word_underscort:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in random_word_list:
            for idx in letter_index[letter]:
                random_word_underscort[idx] = letter
        
        if "_" not in random_word_underscort:
            os.system("clear") 
            print("¡Ganaste! La palabra era", random_word_n)
            break
    
if __name__ == '__main__':
    run()