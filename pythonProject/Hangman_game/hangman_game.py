import random
from os import strerror

def chose_word():
    try:
        with open('new.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            list_words = text.replace(" ", "").split(',')
            number = random.randint(0, len(list_words) - 1)  
            return list_words[number]
    except IOError as e:
        print("Błąd IO", strerror(e.errno))

def check_letter(word):
    count = 0
    word_n = ['_' for _ in range(len(word))] 
    while count <= 8 and True:
        letter = input("Podaj literę: ")

        found = False  
        for index, char in enumerate(word):# umożliwa dostęp jednocześnie do indexu
            if char == letter:
                word_n[index] = letter
                found = True

        if not found:  
            count += 1
            print("Błędna litera. Pozostała liczba prób: ", 8-count)

        print(word_n)
        if "".join(word_n) == word:
            break

    if "".join(word_n) == word:
        print("Gratulacje! Odnalazłeś słowo:", word)
    else:
        print("Przekroczyłeś limit prób. Prawidłowe słowo to:", word)

x = chose_word()
check_letter(x)
