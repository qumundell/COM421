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
            return f"Data: {self.data}, Previous: No previous data, Next: {self.next.data}"
        elif self.next is None:
            return f"Data: {self.data}, Previous: {self.prev.data}, Next: No next data"
        else:
            return f"Data: {self.data}, Previous: {self.prev.data}, Next: {self.next.data}"


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, new_node):
        self.size += 1
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
        if self.size - 1 < index or index < 0:
            print("The given index does not exist in this Linked list")
        else:
            current_node = self.first
            while done is False:
                if count == index:
                    return current_node
                count += 1
                current_node = current_node.next

    def insert_middle(self, new_node, prev_node):
        new_node = Node(new_node)
        current_node = self.first
        done = False
        count = 0
        while done is False:
            if current_node.data == prev_node:
                new_node.link(current_node.next)
                current_node.link(new_node)
                # while done is False:
                # if count == self.last.index:
                self.size += 1
                return "Your item has been added to the List"
                # count += 1
                # current_node = current_node.next
                # current_node.index += 1
            count += 1
            current_node = current_node.next
            if count > current_node.index:
                return "Couldn't find the middle of the given nodes"

    # def remove(self, node_name):
    #     current_node = self.first
    #     while current_node is not None:
    #         if current_node.data == node_name:
    #             if current_node.prev is None:
    #                 self.first = current_node.next
    #                 current_node.next.prev = None
    #             elif current_node.next is None:
    #                 self.last = current_node.prev
    #                 current_node.prev.next = None
    #             else:
    #                 current_node.prev.link(current_node.next)
    #                 current_node.next.link(current_node.prev)

    def __str__(self):
        current_node = self.first
        output = "Contents of Linked List: \n"
        while current_node is not None:
            # for i in range(0, self.last.index+1, 1):
            output = f"{output} {current_node}\n"
            current_node = current_node.next
        return output


n1 = Node("Fred")
n2 = Node("Tom")
n3 = Node("Jim")
ll1 = LinkedList()
ll1.add(n1)
ll1.add(n2)
ll1.add(n3)
print(ll1.insert_middle("Charles", "Tom"))
print(ll1.insert_middle("Jake", "Fred"))
print(ll1)
