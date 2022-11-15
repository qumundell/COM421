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


def dfs(tree, toFind, curNode=None):
    if curNode == None:
        curNode = tree.root
    if curNode.value == toFind:
        print("Your number is in the tree")
        return True
    elif curNode.value < toFind:
        if curNode.right is None:
            return False
        return dfs(tree, toFind, curNode.right)
    elif curNode.value > toFind:
        if curNode.left is None:
            return False
        return dfs(tree, toFind, curNode.left)

bt = BinaryTree()
for val in [32,53,21,12,23,54,23,13,42]:
    bt.insert(val)

userInput = int(input("What number would you want to check for in the tree?"))
if dfs(bt, userInput) is not True:
    print("Your number is not in the tree")