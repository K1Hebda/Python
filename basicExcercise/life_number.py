def life_number(date):
    list_of_numbers = [int(digit) for digit in date if digit.isdigit()]

    while len(list_of_numbers) != 1:
        list_of_numbers = [int(digit) for digit in str(sum(list_of_numbers))]

    return list_of_numbers[0]

date = input("Podaj datę urodzenia (w formacie YYYYMMDD): ")
print("Liczba Życia: " + str(life_number(date)))

a= int("abs")