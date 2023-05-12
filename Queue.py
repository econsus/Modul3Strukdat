class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def print_queue(self):
        for item in self.items:
            print(item, end="")
        print()

    def enqueue_string(self, input_string):
        for char in input_string:
            self.enqueue(char)
            print()
