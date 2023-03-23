class NodeBST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = NodeBST(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = NodeBST(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

#print tree

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


    def inorderTraversal(self, root):
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            print(root.data)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res


#search BST



    def searchBst(self, data):
        # print(self.data)
        if data in self.data.get_lastname() or data in self.data.get_firstname() or data in self.data.get_account_no():
            print('item is found')
            return True

        if data < self.data.get_lastname() or data < self.data.get_firstname() < data in self.data.get_account_no():
            if self.left:
                self.left.searchBst(data)
        else:
            if self.right:
                self.right.searchBst(data)


