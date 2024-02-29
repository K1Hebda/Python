class WyjatekZleDaneStudenta(Exception):
    pass


class ZlaLinia(WyjatekZleDaneStudenta):
    def __init__(self):
        super().__init__("Dane nie zostały podane według schematu")


class PustyPlik(WyjatekZleDaneStudenta):
    def __init__(self):
        super().__init__("Podany plik jest pusty")


dict_data = {}

file_name = input("Podaj nazwę pliku Pana Młodka: ")

try:
    with open(file_name, 'r') as pm:
        line_file = pm.readline()
        if line_file== "":
            raise PustyPlik()
        
        while line_file:
            
            split_file = line_file.split()
            if not (isinstance(split_file[0], str) and isinstance(split_file[1], str) and isinstance(float(split_file[2]), float)):
                raise ZlaLinia()
            
            keys = split_file[0] + " " + split_file[1]
            if keys in dict_data:
                dict_data[keys] += float(split_file[2])
            else:
                dict_data[keys] = float(split_file[2])
                
            line_file = pm.readline()

    sorted_dict = dict(sorted(dict_data.items()))

    # Wydruk danych słownika
    print("Przetworzone dane:")
    for klucz, wartosc in sorted_dict.items():
        print(f"{klucz}: {wartosc}")

except FileNotFoundError as e:
    print("Plik nie istnieje", e)

except PustyPlik as e:
    print("Błąd: ", e)

except ZlaLinia as e:
    print("Błąd: ", e)

except Exception as e:
    print("Wystąpił nieoczekiwany błąd: ", e)
