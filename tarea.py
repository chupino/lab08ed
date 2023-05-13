class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value)
        in_order(node.right)
def caminoLargo(root):
    if root is None:
        return []
    
    pila = [(root, [root.value])]
    caminoLargo = []
    
    while pila:
        node, path = pila.pop()
        
        if node.left is None and node.right is None:
            if len(path) > len(caminoLargo):
                caminoLargo = path
        else:
            if node.left:
                pila.append((node.left, path + [node.left.value]))
            if node.right:
                pila.append((node.right, path + [node.right.value]))
    
    return caminoLargo

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
caminoMasLargo=caminoLargo(root1)
print(caminoMasLargo)

def invertir(root):
    if root is None:
        return None
    root.left,root.right=invertir(root.right),invertir(root.left)
    return root

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)
root2.right.right = Node(7)


arbolInvertido=invertir(root2)
in_order(arbolInvertido)

