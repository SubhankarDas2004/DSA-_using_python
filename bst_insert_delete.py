class Node:
    def __init__(self, item):
        self.info = item
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert_node(self, item):
        nd = Node(item)

        if self.root is None:
            self.root = nd
            return

        temp = self.root

        while True:
            if item < temp.info:
                if temp.left is None:
                    temp.left = nd
                    return
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = nd
                    return
                temp = temp.right

    # Search node
    def search(self, item):
        if self.root == None:
            print("Tree Empty")
            return
        
        temp = self.root

        while temp != None:
            if item == temp.info:
                print("Item found")
                par = temp
                return par, temp

            elif item < temp.info:
                par = temp
                temp = temp.left

            else:
                par = temp
                temp = temp.right

        if temp == None:
            print("Item not found")
            return par, temp
        
    # Deletion of node
    def delete(self, item):

        if self.root == None:
            print("Tree Empty")
            return

        par, temp = self.search(item)

        if temp == None:
            return

        # Case 1 : No child
        if temp.left == None and temp.right == None:

            if par == None:
                self.root = None
                return

            if temp.info < par.info:
                par.left = None
            else:
                par.right = None

        # Case 2 : Only left child
        elif temp.left != None and temp.right == None:

            if par == None:
                self.root = temp.left
                return

            if temp.info < par.info:
                par.left = temp.left
            else:
                par.right = temp.left

        # Case 3 : Only right child
        elif temp.left == None and temp.right != None:

            if par == None:
                self.root = temp.right
                return

            if temp.info < par.info:
                par.left = temp.right
            else:
                par.right = temp.right

        # Case 4 : Both children
        else:

            succ_par = temp
            succ = temp.right

            while succ.left != None:
                succ_par = succ
                succ = succ.left

            temp.info = succ.info

            if succ_par.left == succ:
                succ_par.left = succ.right
            else:
                succ_par.right = succ.right

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.info, end=" ")
            self.inorder(root.right)

    def display(self):
        if self.root is None:
            print("No item found!!")
            return

        self.inorder(self.root)
        print()


bst = BST()

bst.insert_node(50)
bst.insert_node(30)
bst.insert_node(70)
bst.insert_node(20)
bst.insert_node(40)
bst.insert_node(60)
bst.insert_node(80)

bst.search(40)

bst.display()

bst.delete(50)

bst.display()
