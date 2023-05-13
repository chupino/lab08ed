
from ejercicio01 import BinaryTreeNode


def sumRecursive(root):
    if (root == None):
        return 0
    if root.data % 2 == 0:
        return root.data + sumRecursive(root.left) + sumRecursive(root.right)
    else:
        return sumRecursive(root.left) + sumRecursive(root.right)

#
# Resolution
#           1
#       2       3
#     7   5   6   7

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

tmp = sumRecursive(root)
print("La suma del arbol es %d" % (tmp))
