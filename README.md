# unit4-binary-search-trees
CMSC 315 Unit 4 Discussion: Binary Search Trees using Python, recursive insertion, searching, and in-order traversal.
# Unit 4 Discussion: Binary Search Trees (BST)

## Overview

This project demonstrates the implementation of a Binary Search Tree (BST) using Python. It explores recursive insertion, searching, and in-order traversal operations.

A real-world example involving employee ID records was used to demonstrate how a BST organizes and retrieves data efficiently.

## Learning Objectives

- Build a Binary Search Tree.
- Insert values recursively.
- Search for values recursively.
- Perform in-order traversal.
- Understand BST organization and efficiency.
- Test edge cases.

## Implementation

The project implemented the following components:

### 1. Node Class
Created a Node class to store:
- A node value.
- A reference to the left child.
- A reference to the right child.

### 2. Binary Search Tree Class
Implemented a BST class with:
- Tree initialization.
- Recursive insertion.
- Recursive searching.
- In-order traversal.

### 3. Real-World Example

The BST was used to organize employee identification numbers.

The following seven employee IDs were inserted:

`[1050, 1025, 1075, 1010, 1035, 1060, 1090]`

### 4. In-Order Traversal

The in-order traversal visited the left subtree, current node, and right subtree.

The resulting sorted employee IDs were:

`[1010, 1025, 1035, 1050, 1060, 1075, 1090]`

### 5. Search Testing

The following search operations were performed:

| Employee ID | Expected Result | Actual Result |
|---|---|---|
| 1025 | True | True |
| 1060 | True | True |
| 1005 | False | False |
| 1100 | False | False |

### 6. Edge Case Testing

The project also tested:

- Searching an empty tree.
- Traversing an empty tree.
- Inserting a duplicate value.
- Creating a single-node tree.
- Searching for a value in a single-node tree.

All tested cases produced the expected results.

## How to Run

1. Open the project in PyCharm.
2. Navigate to the `unit4_trees` directory.
3. Open the terminal.
4. Execute:

```bash
py unit4_discussion.py
```

## Conclusion

This assignment demonstrated how Binary Search Trees organize information using a hierarchical structure. Recursive insertion and searching allowed values to be placed and retrieved according to their relationship with the current node.

In-order traversal demonstrated how a BST can produce sorted output without requiring an additional sorting algorithm.

The employee ID example illustrated how BSTs can be applied to real-world record management. The edge case tests also helped verify the correctness and reliability of the implementation.

## Technologies Used

- Python 3.14.4
- PyCharm
- Binary Search Trees
- Recursive Algorithms
