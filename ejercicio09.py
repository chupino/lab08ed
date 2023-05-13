class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child

def sumRecursive(root):
    if (root == None):
        return 0
    if root.data % 2 == 0:
        return root.data + sumRecursive(root.left) + sumRecursive(root.right)
    else:
        return sumRecursive(root.left) + sumRecursive(root.right)

def sumLeftNodes(root, isLeft=False):
    if root is None:
        return 0
    
    if isLeft:
        return root.data + sumLeftNodes(root.left, True) + sumLeftNodes(root.right, False)
    else:
        return sumLeftNodes(root.left, True) + sumLeftNodes(root.right, False)
    
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

tmp=sumLeftNodes(root)
print(tmp)