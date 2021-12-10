from structures.node import BinaryNode
from tree import BinaryTree


def numbers_example_tree():
    tree = BinaryTree()
    n1 = BinaryNode(1)
    n2 = BinaryNode(2)
    n3 = BinaryNode(3)
    n4 = BinaryNode(4)
    n5 = BinaryNode(5)
    n6 = BinaryNode(6)
    n7 = BinaryNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    tree.root = n1
    return tree


def math_operation_example_tree():
    """
         '+'
       /     \
     'a'      '*'
             /   \
           'b'    '-'
                 /    \
               '/'    'e'
              /   \
            'c'   'd'

    (a + (b * ((c/d) - e)))
    """
    tree = BinaryTree()
    n1 = BinaryNode('a')
    n2 = BinaryNode('+')
    n3 = BinaryNode('*')
    n4 = BinaryNode('b')
    n5 = BinaryNode('-')
    n6 = BinaryNode('/')
    n7 = BinaryNode('c')
    n8 = BinaryNode('d')
    n9 = BinaryNode('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    return tree


def programmer_example_tree():
    tree = BinaryTree()
    n1 = BinaryNode('P')
    n2 = BinaryNode('R')
    n3 = BinaryNode('O')
    n4 = BinaryNode('G')
    n5 = BinaryNode('R')
    n6 = BinaryNode('A')
    n7 = BinaryNode('M')
    n8 = BinaryNode('M')
    n9 = BinaryNode('E')
    n10 = BinaryNode('X')

    n1.left = n2
    n2.left = n3
    n3.left = n4
    n4.right = n5
    n5.left = n6
    n6.right = n7
    n1.right = n8
    n8.right = n9
    n9.left = n10

    tree.root = n1
    return tree


def geeks_for_geeks_example_tree():
    tree = BinaryTree()
    n1 = BinaryNode(1)
    n2 = BinaryNode(2)
    n3 = BinaryNode(3)
    n4 = BinaryNode(4)
    n5 = BinaryNode(5)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    tree.root = n1
    return tree


if __name__ == "__main__":
    tree = programmer_example_tree()

    print("Pre-order route:")
    tree.preorder_traversal()

    print("\n\nIn-order route:")
    tree.inorder_traversal()

    print("\n\nPost-order route:")
    tree.postorder_traversal()

    print("\nHeight: ", tree.height(tree.root))
