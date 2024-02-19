import time

# Read lines from a file into a list
lines = []
with open('patterns/1000_pattern.txt') as txt:
    for line in txt:
        lines.append(line.strip())

# Define a pattern to search for
pattern = "ABC"
count_1 = 0
count_2 = 0

# Naive pattern matching algorithm
def naive_match(lines, pattern):
    global count_1
    count_1 = 0
    for i in range(len(lines[0]) - 2):
        for j in range(len(lines) - 2):
            if pattern == lines[j][i:i+3]:
                if pattern == lines[j][i] + lines[j+1][i] + lines[j+2][i]:
                    count_1 += 1
                    # print("coordinates:", j, ",", i)

# Rabin-Karp pattern matching algorithm
def rabin_karp_match(lines, pattern, d=16, prime_n=101):
    global count_2
    count_2 = 0
    n = len(lines[0])
    m = len(pattern)
    H = pow(d, m-1) % prime_n
    p = 0
    ts = [0] * n

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime_n
        for j in range(n-2):
            ts[j] = (d * ts[j] + ord(lines[j][i])) % prime_n

    for i in range(n-m+1):
        for j in range(n-m+1):
            if p == ts[j]:
                if pattern == lines[j][i:i+m]:
                    if pattern == lines[j][i] + lines[j+1][i] + lines[j+2][i]:
                        count_2 += 1
                        # print(f"coordinates {j, i}")
            if i < n-m:
                ts[j] = (d*(ts[j]-ord(lines[j][i])*H) + ord(lines[j][i+m])) % prime_n

# Measure the time taken by each algorithm for 6 iterations
time_1 = []
time_2 = []
for i in range(6):
    stime = time.time()
    rabin_karp_match(lines, pattern)
    time_1.append(time.time() - stime)

    ztime = time.time()
    naive_match(lines, pattern)
    time_2.append(time.time() - ztime)

# Calculate the mean time for each algorithm
mean_1 = sum(time_1) / 6
mean_2 = sum(time_2) / 6

# Print the results
print("Search time, naive algorithm: ", mean_1)
print("Search time, Rabin-Karp algorithm: ", mean_2)

# Print the counts of matches found by each algorithm
print(count_1)
print(count_2)
