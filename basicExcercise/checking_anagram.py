def checking_anagram(word1, word2):
    sorted_word1 = ''.join(sorted(word1.upper()))
    sorted_word2 = ''.join(sorted(word2.upper()))
    
    if sorted_word1 == sorted_word2:
        print("Podane słowa to anagram!! ")
    else:
        print("Podane słowa nie są anagramem :(")

word1 = input("Podaj pierwsze słowo: ")
word2 = input("Podaj anagram do poprzedniego słowa: ") 
checking_anagram(word1, word2)
