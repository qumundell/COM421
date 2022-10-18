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
        if  self.current_size == len(self.internalArray): #if queue is not too full
            return "The given command was not possible due to an excess of objects in the queue"
        else:
            self.internalArray[self.end] = new_item
            if self.end == len(self.internalArray) - 1: #if end of queue is at the end of the array
                self.end = 0
                self.current_size += 1
            else:
                self.end += 1
                self.current_size += 1
            return "The given command has been executed"

    def __str__(self):
        return f"{self.internalArray.__str__}\nStarting at: {self.front}\nEnding at: {self.end}"
