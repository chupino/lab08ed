class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child

def findMaxRecursive(tree): 
      
    # Base case  
    if tree is None:  
        return float('-inf')  # Mininum value

    data = tree.data 
    left_max = findMaxRecursive(tree.left)  
    right_max = findMaxRecursive(tree.right)  
        
    return max([data, left_max, right_max])
def findMinRecursive(tree): 
      
    # Base case  
    if tree is None:  
        return float('-inf')  # Mininum value

    data = tree.data 
    left_max = findMaxRecursive(tree.left)  
    right_max = findMaxRecursive(tree.right)  
        
    return min([data, left_max, right_max])

childLeftLeft=BinaryTreeNode(4)
childLeftRight=BinaryTreeNode(7)
childRightLeft=BinaryTreeNode(8)
childRightRight=BinaryTreeNode(5)
childLeft=BinaryTreeNode(2,childLeftLeft,childLeftRight)
childRight=BinaryTreeNode(3,childRightLeft,childRightRight)
root=BinaryTreeNode(1,childLeft,childRight)
maxData = findMaxRecursive(root)
minData = findMinRecursive(root)
print(maxData)
print(minData)