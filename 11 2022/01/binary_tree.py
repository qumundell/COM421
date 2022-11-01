class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, value, curNode=None):
        if self.root.value is None:
            self.root.value = value
        else:
            if curNode is None:
                curNode = self.root
            if value > curNode.value:
                if curNode.right is None:
                    curNode.right = TreeNode(value)
                else:
                    self.insert(value, curNode.right)
            else:
                if curNode.left is None:
                    curNode.left = TreeNode(value)
                else:
                    self.insert(value, curNode.left)

    def print_from(self, curNode=None):
        if curNode is None:
            curNode = self.root
        if curNode.left is not None:
            self.print_from(curNode.left)
        print(curNode.value)
        if curNode.right is not None:
            self.print_from(curNode.right)


bt = BinaryTree()
bt.insert(20)
bt.insert(16)
bt.insert(25)
bt.insert(23)
bt.insert(33)
bt.insert(1)
bt.print_from()
