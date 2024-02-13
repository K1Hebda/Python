from time import time
from random import randint

# Function to perform Insertion Sort on a list
def insert_sort(A):
    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x

# Function to perform Merge Sort on a list
def merge_sort(A, a, b):
    if a < b:
        c = (a + b) // 2
        merge_sort(A, a, c)
        merge_sort(A, c + 1, b)

        A_ = []
        i = a
        j = c + 1
        while i <= c and j <= b:
            if A[i] < A[j]:
                A_.append(A[i])
                i += 1
            else:
                A_.append(A[j])
                j += 1

        while i <= c:
            A_.append(A[i])
            i += 1

        while j <= b:
            A_.append(A[j])
            j += 1

        for k in range(len(A_)):
            A[a + k] = A_[k]

# Main part of the program
list1 = []
n = int(input('Enter the number of elements in the sequence: '))

# Generating 101 lists of random integers
for i in range(101):
    lst = []
    for j in range(n):
        lst.append(randint(0, n))
    list1.append(lst)
list2 = list1.copy()

insert_sort_time = []
merge_sort_time = []

# Timing the execution of Insertion Sort and Merge Sort on each list
for i in range(101):
    start_time = time()
    insert_sort(list1[i])
    insert_sort_time.append(time() - start_time)

    start_time = time()
    merge_sort(list2[i], 0, len(list2[i]) - 1)
    merge_sort_time.append(time() - start_time)

# Calculating statistics based on the timing results
merge_mean = sum(merge_sort_time) / 101
insert_mean = sum(insert_sort_time) / 101
proportion = insert_mean / merge_mean
merge_max = max(merge_sort_time)
merge_min = min(merge_sort_time)
insert_max = max(insert_sort_time)
insert_min = min(insert_sort_time)

# Displaying the results
print('insert_sort time:', insert_mean)
print('merge_sort time: ', merge_mean)
print('proportion: ', proportion)
print('Maximum merge_sort time: ', merge_max, ', minimum time: ', merge_min)
print('Maximum insert_sort time: ', insert_max, ', minimum time: ', insert_min)
