def checking_palindrome(text):
    text=text.lower()
    text=text.replace(" ", "")
    reverse_text= text[::-1]
    if text == reverse_text:
        print("Tak, tekst jest palindromem")
        print(reverse_text)
    else:
        print("Niestety tekst nie jest palindromem")
        print(reverse_text)
    
    

text=input("podaj palindrom: ")
checking_palindrome(text)
