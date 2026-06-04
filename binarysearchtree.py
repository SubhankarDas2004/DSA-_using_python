class node:
    def __init__(self, item):
        self.info=item
        self.left=None
        self.right=None

class BinarySTree:
    def __init__(self):
        self.root=None
    def insert(self, item):
        nd=node(item)
        if self.root==None:
            self.root=nd
            return
        temp=self.root
        while temp!=None:
            if item<temp.info:
                parent=temp
                temp=temp.left
            else:
                parent=temp
                temp=temp.right
        if item<parent.info:
            parent.left=nd
        else:
            parent.right=nd

    def inorder(self,nd):
        if nd!=None:
            self.inorder(nd.left)
            print(nd.info,end=" ")
            self.inorder(nd.right)

    def postorder(self,nd):
        if nd!=None:

            self.inorder(nd.left)
            self.inorder(nd.right)
            print(nd.info,end=" ")

            
    def preorder(self,nd):
        if nd!=None:
            print(nd.info,end=" ")
            self.inorder(nd.left)
            self.inorder(nd.right)

bst=BinarySTree()
bst.insert(100)
bst.insert(80)
bst.insert(110)
bst.insert(150)
bst.insert(67)
print("Tree in inorder form:\n")
bst.inorder(bst.root)
print("\nTree in postorder form:\n")
bst.postorder(bst.root)
print("\nTree in preorder form:\n")
bst.preorder(bst.root)
        
