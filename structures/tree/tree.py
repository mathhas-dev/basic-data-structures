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
        # If no nodes were provided, use root node.
        if node is None:
            node = self.root

        h_left = 0
        h_right = 0

        # Traversal all left nodes
        if node.left:
            h_left = self.height(node.left)
        # Traversal all right nodes
        if node.right:
            h_right = self.height(node.right)

        # Returns the biggest height
        return max(h_left, h_right)

    def preorder_traversal(self, node=None):
        """
        Algorithm:
            1. Visit the root.
            2. Traverse the left subtree, call Preorder(left-subtree)
            3. Traverse the right subtree, call Preorder(right-subtree) 
        """
        pass

    def inorder_traversal(self, node=None):
        """
        Algorithm:
            1. Visit the root.
            2. Traverse the left subtree, call Preorder(left-subtree)
            3. Traverse the right subtree, call Preorder(right-subtree) 
        """
        pass

    def postorder_traversal(self, node=None):
        """
        Algorithm:
            1. Traverse the left subtree, call Postorder(left-subtree)
            2. Traverse the right subtree, call Postorder(right-subtree)
            3. Visit the root.
        """
        pass
