# unit4-binary-search-trees
CMSC 315 Unit 4 Discussion: Binary Search Trees using Python, recursive insertion, searching, and in-order traversal.
# Unit 4 Discussion: Binary Search Trees (BST)

## Overview

This will give you an example of how to implement a Binary Search Tree (BST) in Python. It discusses recursive insertion, searching and in-order traversal operations.

To show how a BST can efficiently organize and retrieve data, a real-life example of employee ID records was used.


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

This assignment showed the application of information hierarchy to Binary Search Trees. The recursive insertion and search operations enabled the values to be inserted and retrieved based on their relationship to the current node.

We saw how to use in-order traversal to get the output sorted without having to use any other sorting algorithm with a BST.

The example of the employee ID showed how BSTs can be used in a practical application of record management. The boundary value tests were also used to ensure the correctness and reliability of the implementation.


