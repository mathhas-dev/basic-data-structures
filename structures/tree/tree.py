from structures.node import BinaryNode


class BinaryTree:

    def __init__(self, data=None, node=None) -> None:
        if data:
            self.root = BinaryNode(data)
        elif node:
            self.root = node
        else:
            self.root = None

    def height(self, node=None):
        """
        Return the height of the tree
        (ends the recursion when there is no more child node)
        """
        # Checks if binary tree is empty
        if node is None:
            return 0

        # Traversal all left nodes
        h_left = self.height(node.left)
        # Traversal all right nodes
        h_right = self.height(node.right)

        # Returns the biggest height
        return max(h_left, h_right) + 1

    def preorder_traversal(self, node=None):
        """
        Algorithm:
            1. Visit the root.
            2. Traverse the left subtree, call Preorder(left-subtree)
            3. Traverse the right subtree, call Preorder(right-subtree) 
        """
        if node is None:
            node = self.root

        print(node.data, end="")
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        """
        Algorithm
            1. Traverse the left subtree, call Inorder(left-subtree)
            2. Visit the root.
            3. Traverse the right subtree, call Inorder(right-subtree)
        """
        if node is None:
            node = self.root

        if node.left:
            self.inorder_traversal(node.left)
        print(node.data, end="")
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        """
        Algorithm:
            1. Traverse the left subtree, call Postorder(left-subtree)
            2. Traverse the right subtree, call Postorder(right-subtree)
            3. Visit the root.
        """
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.data, end="")

    # TODO:
    # https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/


class BinarySearchTree(BinaryTree):
    # TODO: Implement binary search tree
    pass
