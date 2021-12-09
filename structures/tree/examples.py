from structures.node import BinaryNode
from tree import BinaryTree


def height_example_tree():
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


def inorder_example_tree():
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


def postorder_example_tree():
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
    n0 = BinaryNode('R')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree


if __name__ == "__main__":
    # tree = inorder_example_tree()

    # print("In-order route:")
    # tree.inorder_example_tree

    # tree = postorder_example_tree()
    # print("Post-order route:")

    # tree.postorder_traversal()

    tree = height_example_tree()
    print("Height: ", tree.height(tree.root))

