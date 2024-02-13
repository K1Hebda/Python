# Tower of Hanoi Algorithm

This repository contains Python implementations of both recursive and iterative solutions for the Tower of Hanoi problem. The Tower of Hanoi is a classic algorithmic problem that involves moving a tower of disks from one rod to another, with the constraint that larger disks cannot be placed on top of smaller ones.

## Implementation Details

### Recursive Algorithm

The recursive implementation of the Tower of Hanoi algorithm is provided in the function `hanoi_recursive`. It counts the number of steps (`step1`) and prints the sequence of moves.

### Iterative Algorithm

The iterative implementation of the Tower of Hanoi algorithm is provided in the function `hanoi_iterative`. It counts the number of steps (`step2`) and prints the sequence of moves. The algorithm uses a while loop and follows the "divide and conquer" approach.

## How to Use

1. Input the number of elements for the Hanoi tower when prompted.
2. The program initializes towers for both recursive and iterative approaches.
3. It records the start time and executes the recursive Hanoi algorithm.
4. It records the start time and executes the iterative Hanoi algorithm.
5. The results, including the reversed disks and algorithm execution time, are displayed.

## Performance Comparison

The code includes functionality to compare the execution times of both recursive and iterative implementations. The goal is to evaluate the efficiency of each algorithm based on the number of disks. The results will help you understand which implementation performs better in different scenarios.
