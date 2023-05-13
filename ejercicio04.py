class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child
def preOrderRecursive(root, result):

    if not root:
        return

    result.append(root.data)
    preOrderRecursive(root.left, result)
    preOrderRecursive(root.right, result)

def postOrderRecursive(root, result):

    if not root:
        return

    postOrderRecursive(root.left, result)
    postOrderRecursive(root.right, result)
    result.append(root.data)

childLeftLeft=BinaryTreeNode("4")
childLeftRight=BinaryTreeNode("5")
childRightLeft=BinaryTreeNode("6")
childRightRight=BinaryTreeNode("7")
childLeft=BinaryTreeNode("2",childLeftLeft,childLeftRight)
childRight=BinaryTreeNode("3",childRightLeft,childRightRight)
root=BinaryTreeNode("1",childLeft,childRight)
result=[]
postOrderRecursive(root=root,result=result)
print(result)