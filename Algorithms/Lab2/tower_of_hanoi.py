import time

# Initialize global step counters
step1 = 0
step2 = 0

# Recursive implementation of the Hanoi algorithm
def hanoi_recursive(n, source, destination, buffer):
    global step1

    if n == 1:
        step1 += 1
        destination.append(source.pop())
    else:
        hanoi_recursive(n - 1, source, buffer, destination)
        step1 += 1
        destination.append(source.pop())
        hanoi_recursive(n - 1, buffer, destination, source)

# Iterative implementation of the Hanoi algorithm
def hanoi_iterative(n, source, destination, buffer):
    global step2

    if n % 2 == 0:
        destination, buffer = buffer, destination

   # while source or destination :
    while not (len(destination) == n or len(buffer) == n) :

        if step2 % 3 == 0:
            if source and (not destination or source[-1] < destination[-1]):
                destination.append(source.pop())
                step2 += 1
            elif destination and (not source or destination[-1] < source[-1]):
                source.append(destination.pop())
                step2 += 1

        if step2 % 3 == 1:
            if source and (not buffer or source[-1] < buffer[-1]):
                buffer.append(source.pop())
                step2 += 1
            elif buffer and (not source or buffer[-1] < source[-1]):
                source.append(buffer.pop())
                step2 += 1

        if step2 % 3 == 2:
            if buffer and (not destination or buffer[-1] < destination[-1]):
                destination.append(buffer.pop())
                step2 += 1
            elif destination and (not buffer or destination[-1] < buffer[-1]):
                buffer.append(destination.pop())
                step2 += 1


        

# Input the number of elements for the Hanoi tower
n = int(input("How many elements does the Hanoi tower have? "))

# Initialize towers for both recursive and iterative approaches
source_recursive = list(range(1, n + 1))[::-1]
source_iterative = list(range(1, n + 1))[::-1]

destination_recursive = []
buffer_recursive = []
destination_iterative = []
buffer_iterative = []

# Record the start time and execute the recursive Hanoi algorithm
start_time = time.perf_counter()
hanoi_recursive(n, source_recursive, destination_recursive, buffer_recursive)
time_recursive = time.perf_counter() - start_time

# Record the start time and execute the iterative Hanoi algorithm
start_time = time.perf_counter()
hanoi_iterative(n, source_iterative, destination_iterative, buffer_iterative)
time_iterative = time.perf_counter() - start_time

# Display the results
print("Reversed disks (recursive) in", step1, "steps:", destination_recursive, "Algorithm execution time:", time_recursive)
print("Reversed disks (iterative) in", step2, "steps:", destination_iterative, "Algorithm execution time:", time_iterative)
