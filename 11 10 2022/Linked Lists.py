class Node:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.prev = None
        self.next = None

    def link(self, new_node):
        self.next = new_node
        new_node.prev = self
        new_node.index = self.index + 1

    def __str__(self):
        if self.prev is None:
            return f"Previous: No previous data, Next: {self.next.data}, Data: {self.data}"
        elif self.next is None:
            return f"Previous: {self.prev.data}, Next: No next data, Data: {self.data}"
        else:
            return f"Previous: {self.prev.data}, Next: {self.next.data}, Data: {self.data}"


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, new_node):
        if self.first is None:
            self.first = new_node
            self.last = new_node
            new_node.index = 0
        else:
            self.last.link(new_node)
            self.last = new_node

    def get(self, index):
        done = False
        count = 0
        if self.last.index < index or index < 0:
            print("The given index does not exist in this Linked list")
        else:
            current_node = self.first
            while done is False:
                if count == index:
                    return current_node
                count += 1
                current_node = current_node.next

    def insert_middle(self, new_node, prev_node):
        current_node = self.first
        done = False
        count = 0
        while done is False:
            if current_node.data == prev_node:
                current_node.link(prev_node)
                prev_node.link(current_node.next)
                while done is False:
                    if count == self.last.index:
                        return current_node
                    count +=1
            count += 1
            current_node = current_node.next
            if count > current_node.index:
                return "Couldn't find the middle of the given nodes"


n1 = Node("Fred")
n2 = Node("Tom")
n3 = Node("Jim")
ll1 = LinkedList()
ll1.add(n1)
ll1.add(n2)
ll1.add(n3)
print(ll1.get(1))
