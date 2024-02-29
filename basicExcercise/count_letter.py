from os import strerror

file_name = input("Podaj nazwę pliku wejściowego: ")

# Zakres od 'a' do 'z' + 1, aby uwzględnić 'z'
count_letter = {}
for i in range(ord('a'), ord('z') + 1):
    count_letter[chr(i)] = 0

try:
    with open(file_name, 'rt') as file:
        while True:
            char_l = file.read(1).lower()
            if not char_l:
                break
            value = ord(char_l)
            if ord('a') <= value <= ord('z'):
                count_letter[char_l] += 1

except Exception as exc:
    print("Plik nie mógł zostać otwarty:", strerror(exc.errno))

sorted_count_letters = dict(sorted(count_letter.items(), key=lambda item: item[1], reverse=True))

# Wyświetlanie histogramu
print("Histogram wystąpień liter:")
for char, count in sorted_count_letters.items():
    if count > 0:
        print(f"{char}: {count}")

# Zapisz histogram do pliku
histogram_file_name = file_name + ".hist"
try:
    with open(histogram_file_name, 'wt') as hist_file:
        for char, count in sorted_count_letters.items():
            if count > 0:
                hist_file.write(f"{char}: {count}\n")

except Exception as exc:
    print("Nie udało się zapisać histogramu do pliku:", strerror(exc.errno))