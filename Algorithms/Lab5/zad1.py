from math import sqrt
from time import time

cities = []
with open('TSP.txt') as txt:
    for line in txt:
        index, x, y = map(float, line.split()) #przekształca każda liczbę w tekście na float i przypisuje do zmienncyh 
        cities.append((x, y))

#funkcja wyznacza odległość między dwoma miastami
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

#znajduje najbliższe miasto do danego miasta
def find_nearest_city(city, cities):
    nearest_city = None
    smallest_distance = float('inf')   #inicjalizuje zmienna jako nieskończoność, żeby móc poźniej przechowywać najmniejsza odległo
    for c in cities:
        distance = calculate_distance(city, c)
        if distance < smallest_distance:
            smallest_distance = distance
            nearest_city = c
    return nearest_city

#wyznacza ścieżkę
def find_path(cities):
    cities_copy = cities.copy()
    path = [cities_copy.pop(0)]
    while cities_copy:
        city = find_nearest_city(path[-1], cities_copy)
        path.append(city)
        cities_copy.remove(city)
    return path

stime=time()
path = find_path(cities)
serch_time=time()-stime

#obliczanie długości ścieżki
def road_length(cities):
    distance = 0
    for j in range(len(cities)-1):
        distance += calculate_distance(cities[j], cities[j+1])
    distance += calculate_distance(cities[0], cities[-1])
    return distance

#długośc ścieżki w kolejności jak w pliku tekstowym
x = road_length(cities)

#długośc wyznaczonej ścieżki za pomocą algorytmu najbliższego sąsiada
y = road_length(path)

print("długość drogi przecchodząc każde miasto po kolei: ",x)
print("długość drogi wyznaczonej przez algorytm najbliższego sąsiada: ", y, "czas trwania wyszukiwania: ", serch_time)