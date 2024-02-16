import random
import time

class Node:
    def __init__(self, value):
        # Node initialization with a given value
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, N):
        # Creating roots with values from 0.5 to N + 0.5 with a step of 1.0
        self.roots = [Node(0.5 + value) for value in range(0, N)]

    def insert(self, value):
        # Inserting a value into the appropriate subtree
        for root in self.roots:
            if abs(root.value - value) <= 0.5:
                self._insert(root, value)
                break

    def _insert(self, node, value):
        # Choosing whether the value goes to the left or right node
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                # If the left node exists, recursively call the _insert method
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
   
    def print(self, node=None, depth=0):
        # Printing the tree structure
        if node is None:
            for root in self.roots:
                self.print(root, depth)
                print()
        else:
            if node.right:
                self.print(node.right, depth + 1)
            print(' ' * depth + '-' * depth + str(node.value))
            if node.left:
                self.print(node.left, depth + 1)

    def minimum(self):
        # Finding the minimum value in the entire tree
        min_node = None
        for root in self.roots:
            node = root
            while node.left is not None:
                node = node.left
            if min_node is None or node.value < min_node.value:
                min_node = node
        return min_node

    def maximum(self):
        # Finding the maximum value in the entire tree
        max_node = None
        for root in self.roots:
            node = root
            while node.right is not None:
                node = node.right
            if max_node is None or node.value > max_node.value:
                max_node = node
        return max_node
    
    def find_node(self, x):
        # Searching for a node with value x in the entire tree
        for root in self.roots:
            node = root
            while node is not None:
                if node.value == x:
                    return node
                elif x < node.value:
                    node = node.left
                else:
                    node = node.right
        return None

# Input for the number of roots
N = int(input("Enter the number of roots: "))
# Creating an instance of BST
x = BST(N)
# Input for the number of elements to add to the tree
n = int(input("How many elements do you want to add to the tree: "))

values_ = []
values_round = []
for i in range(n):
    # Generating random values and rounding to 2 decimal places
    values_.append(random.uniform(0, N))
    values_round.append(round(values_[i], 2))

# Checking the execution time of various operations
stime = time.perf_counter()
for value in values_round:
    x.insert(value)
insertion_time = time.perf_counter() - stime

stime = time.perf_counter()
minimum_node = x.minimum()
min_time = time.perf_counter() - stime

stime = time.perf_counter()
maximum_node = x.maximum()
max_time = time.perf_counter() - stime

x.print()

# Input for the element to search for
z = float(input("Enter the element you want to search for: "))
stime = time.perf_counter()
found_node = x.find_node(z)
found_time = time.perf_counter() - stime

# Displaying values and results
print("Minimum value in the selected subtree:", minimum_node.value)
print("Maximum value in the selected subtree:", maximum_node.value)

if found_node is not None:
    print("Node found:", found_node.value)
else:
    print("Node not found")

print("Insertion time: " , insertion_time)
print("Maximum search time: ", max_time)
print("Minimum search time: ", min_time)
print("Search time: ", found_time)
