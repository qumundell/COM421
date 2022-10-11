class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        self.internalArray.append(item)

    def pop(self):
        if len(self.internalArray) >= 1:
            value = self.internalArray[-1]
            del self.internalArray[-1]
            return value
        else:
            return "The stack has no items in it"

    def peek(self):
        if len(self.internalArray) >= 1:
            return self.internalArray[-1]
        else:
            return "The stack has no items in it"

    def __str__(self):
        return self.internalArray.__str__()


stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
print(stack1)
popped1 = stack1.pop()
print(popped1)
popped2 = stack1.pop()
print(popped2)

stack2 = Stack()
stack2.push("Linux")
stack2.push("Windows")
stack2.push("Mac OS X")
print(stack2)
