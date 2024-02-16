# Binary Search Tree (BST) Implementation

This repository contains a Python implementation of a Binary Search Tree (BST) with insertion, min/max search, and visualization features.

## Implementation Details

### Binary Search Tree (BST)

- Efficient storage of unsorted datasets using a binary search tree structure.
- Implemented insertion, min/max search, and visualization features.

### Operations

- **Insertion:** Capability to insert values into the BST, organizing them based on the binary search tree rules.
- **Minimum and Maximum Search:** Operations to find the minimum and maximum values in the entire tree.
- **Visualization:** Textual representation of the BST structure for clear hierarchy visualization.

## How to Use

1. Input the number of roots when prompted.
2. Specify the desired number of elements to add to the tree.
3. Random data will be generated within the specified range and rounded.
4. Test insertion, minimum, maximum, and search operations on the created BST.
5. View the printed tree structure in the console.

## Summary

- **Computational Complexity:** 
  - The time complexity of operations grows logarithmically with the number of elements in a complete binary tree (O(log n)).
  - The presence of incomplete trees can introduce variability in the computational complexity, especially when the tree becomes more diverse in height.
  - In the worst-case scenario, where the tree becomes a single long subtree, the computational complexity can reach O(n).