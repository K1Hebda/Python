# Szyfr Cezara
def cezar_encryption(tekst,liczba_przesuniec):
    tekst=list(tekst)
    szyfr = ''
    
    for char in tekst:
        kod=ord(char)
        if char.isalpha():
            if char.islower():
                kod = ord(char) + liczba_przesuniec
                if kod > ord('z'):
                    kod = ord('a')+kod-ord('z')
                    
            if char.isupper():
                kod = ord(char) + liczba_przesuniec
                if kod > ord('Z'):
                    kod = ord('A')+kod-ord('Z')
                
        szyfr += chr(kod)
    
    return szyfr
    
    
def cezar_decoding(encrypted_tekst,liczba_przesuniec):
    encrypted_tekst=list(encrypted_tekst)
    szyfr = ''
    
    for char in encrypted_tekst:
        kod=ord(char)
        if char.isalpha():
            if char.islower():
                kod = ord(char) - liczba_przesuniec
                if kod < ord('a'):
                    kod = ord('z')-ord('a')+kod
                    
            if char.isupper():
                kod = ord(char) - liczba_przesuniec
                if kod < ord('A'):
                    kod = ord('Z')-ord('A')+kod
                
        szyfr += chr(kod)
    
    return szyfr


tekst = input("Wpisz wiadomosc: ")
liczba_przesuniec=0

while True:
    try:
        liczba_przesuniec = int(input("Podaj liczbę z zakresu 1-25, która będzie określała przesunięcie w kodzie ASCII: "))
        if 1 <= liczba_przesuniec <= 25:
            break  # Wychodzimy z pętli, jeśli liczba jest poprawna
        else:
            print("Podana liczba musi być z zakresu 1-25.")
    except ValueError:
        print("Podana wartość musi być liczbą całkowitą.")

coded_text=cezar_encryption(tekst,liczba_przesuniec)
print(coded_text)
print(cezar_decoding(coded_text,liczba_przesuniec))