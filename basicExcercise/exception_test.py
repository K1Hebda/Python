def readint(prompt, min, max):
    try:
        number= int(input(prompt))
        assert number>= min
        assert number<= max
    except ValueError:
        print("Podana liczba nie jest liczbą całkowitą.")
    except AssertionError:
        print("Podana liczba nie należy do podanego zakresu")
    except:
        print("Jakiś inny błąd")

    return number


v = readint("Podaj liczbe od -10 do 10: ", -10, 10)

print("Liczba to:", v)
