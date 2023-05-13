class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child
def findDataRecursive(root, dataSearch, nro_times=0):

    if root == None:
        return nro_times

    tmp_nro_times = nro_times

    if root.data == dataSearch:
        tmp_nro_times +=1
    
    return  tmp_nro_times  +  \
        findDataRecursive(root.left, dataSearch, nro_times)  + \
        findDataRecursive(root.right, dataSearch, nro_times)

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

dataSearch = 10
nro_times = findDataRecursive(root, dataSearch)
print("Se encontro el valor de %d, %d veces" % (dataSearch, nro_times))
