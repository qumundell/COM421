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


class Queue:
    def __init__(self, size):
        self.internalArray = [None] * size
        self.end = 0
        self.front = 0
        self.current_size = 0

    def remove(self):
        if self.current_size == 0:
            return "The given command was not possible due to a lack of objects in the queue"
        else:
            item = self.internalArray[self.front]
            self.internalArray[self.front] = None
            self.front += 1
            self.current_size -= 1
            print("The given command has been executed")
            return item

    def add(self, new_item):
        if self.current_size == len(self.internalArray):
            return "The given command was not possible due to an excess of objects in the queue"
        else:
            self.internalArray[self.end] = new_item
            if self.end == len(self.internalArray) - 1:
                self.end = 0
                self.current_size += 1
            else:
                self.end += 1
                self.current_size += 1
            return "The given command has been executed"

    def __str__(self):
        return f"{self.internalArray.__str__()}\nStarting at: {self.front}\nEnding at: {self.end - 1}"


def breadthFirstSearch(tree, toFind):
    pass

bt = BinaryTree
for val in [32,53,21,12,23,54,23,13,42]:
    bt.insert(val)

breadthFirstSearch(bt, 13)