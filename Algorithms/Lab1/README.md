# Sorting Algorithms Comparison

This repository contains Python implementations of Insertion Sort and Merge Sort algorithms, along with a program to compare their execution times on a sequence of lists.

## Implementation Details

### Insertion Sort

The `insert_sort` function performs the Insertion Sort algorithm on a given list. It iterates through the list, compares elements, and inserts each element into its proper position.

### Merge Sort

The `merge_sort` function performs the Merge Sort algorithm on a given list within a specified range. It divides the list into halves, recursively sorts them, and then merges the sorted halves.

## How to Use

1. Input the number of elements in the sequence when prompted.
2. The program generates 101 lists of random integers.
3. It applies Insertion Sort and Merge Sort to each list, measuring their execution times.
4. Statistics on execution times are calculated and displayed.

## Timing Results

The program times the execution of Insertion Sort and Merge Sort on each of the 101 generated lists. It calculates the mean execution times, the proportion of Insertion Sort time to Merge Sort time, and identifies maximum and minimum execution times.

## Performance Comparison Insights

For random numerical sequences containing a large number of elements, the Mergesort algorithm proves to be faster than Insertsort. As the number of elements in the sequence increases, the ratio of execution time between Mergesort and Insertsort noticeably grows. Insertsort has lower stack space requirements, but its time complexity increases more rapidly with a higher number of elements. Mergesort, despite requiring more stack space to store subsequences, demonstrates greater efficiency for larger datasets due to its superior time complexity.