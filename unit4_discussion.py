"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
            self.value = value
            self.left = None
            self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
            self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If the current position is empty, create a new node.
        if node is None:
            return Node(value)

        # Smaller values go into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values go into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the updated node.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If the current node is empty, the value does not exist.
        if node is None:
            return False

        # If the current node contains the target, it was found.
        if value == node.value:
            return True

        # If the target is smaller, search the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Otherwise, search the right subtree.
        return self._search_recursive(node.right, value)
    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Stop when an empty child position is reached.
        if node is not None:

            # First, visit the left subtree (smaller values).
            self._inorder_recursive(node.left, values)

            # Second, add the current node's value.
            values.append(node.value)

            # Third, visit the right subtree (larger values).
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # Create a Binary Search Tree for employee ID records.
    employee_tree = BST()

    # Insert seven employee IDs in a middle-first order.
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090]

    for employee_id in employee_ids:
        employee_tree.insert(employee_id)

    # A balanced insertion order helps reduce the search space.
    print("Employee IDs inserted:", employee_ids)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    # Display employee IDs in ascending order.
    sorted_ids = employee_tree.inorder()
    print("Employee IDs in sorted order:", sorted_ids)

    # In-order traversal visits left, current node, then right.
    # This produces sorted output because of the BST ordering rule.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Search for two employee IDs that exist in the tree.
    print("Searching for employee ID 1025:", employee_tree.search(1025))
    print("Searching for employee ID 1060:", employee_tree.search(1060))

    # Search for two employee IDs that do not exist.
    print("Searching for employee ID 1005:", employee_tree.search(1005))
    print("Searching for employee ID 1100:", employee_tree.search(1100))

        # Existing IDs return True, while missing IDs return False.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Search and traversal in an empty tree.
    empty_tree = BST()

    print("Empty tree traversal:", empty_tree.inorder())
    print("Searching empty tree for 1050:", empty_tree.search(1050))

    # An empty tree has no root, so traversal returns an empty list
    # and searching returns False.

    # Edge case 2: Insert a duplicate employee ID.
    employee_tree.insert(1050)

    print("Traversal after duplicate insertion:", employee_tree.inorder())

    # Duplicate IDs are ignored because our insertion method
    # only inserts values that are smaller or larger.

    # Edge case 3: Create a tree containing only one node.
    single_tree = BST()
    single_tree.insert(2000)

    print("Single-node tree traversal:", single_tree.inorder())
    print("Searching for 2000:", single_tree.search(2000))



if __name__ == "__main__":
    main()