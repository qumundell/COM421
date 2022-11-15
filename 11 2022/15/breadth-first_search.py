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

    def cur_front(self):
        return self.internalArray[self.front]
    def remove(self):
        if self.current_size == 0:
            return "The given command was not possible due to a lack of objects in the queue"
        else:
            item = self.internalArray[self.front]
            self.internalArray[self.front] = None
            self.front += 1
            self.current_size -= 1
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
    done = False
    qu = Queue(20)
    qu.add(tree.root)
    while done is False:
        if tree.root.value == None:
            done = True
            print("The given tree is empty")
        elif qu.cur_front() is None:
            done = True
            print("The item to find does not exist")
        else:
            if qu.cur_front() is None:
                done = True
                print("The item to find does not exist")
            if qu.cur_front().left is not None:
                qu.add(qu.cur_front().left)
            if qu.cur_front().right is not None:
                qu.add(qu.cur_front().right)
            if qu.cur_front().value == toFind:
                done = True
                print("The item to find is in the list")
            qu.remove()


bt = BinaryTree()
for val in [32,53,21,12,23,54,23,13,42]:
    bt.insert(val)

userInput = int(input("What number would you want to check for in the list?"))
breadthFirstSearch(bt, userInput )