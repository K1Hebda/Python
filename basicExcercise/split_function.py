def mysplit(strng):
    words = []
    word = ''

    for i, char in enumerate(strng):
        strng = strng.strip(" ")  # Poprawka 1: Usunięcie zbędnych białych znaków
        if char.isspace():
            if word:  # Sprawdzenie, czy słowo nie jest puste
                words.append(word)
                word = ''
        else:
            word += char

        if i == len(strng) - 1:
            if word:  # Sprawdzenie, czy słowo nie jest puste
                words.append(word)

    return words
            


print(mysplit("Być albo nie być, oto jest pytanie"))
print(mysplit("Być albo nie być,oto jest pytanie"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
