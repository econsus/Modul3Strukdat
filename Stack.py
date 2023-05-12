class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, item):
        if isinstance(item, str):
            for letter in item:
                self.top += 1
                self.items.append(letter)
        else:
            self.top += 1
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.items.pop()
        else:
            print("Stack Kosong!")

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]
        else:
            print("Stack Kosong!")

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def print_stack_reverse(self):
        print(" ".join(str(item) for item in reversed(self.items[::-1])))

    def print_stack(self):
        print(" ".join(str(item) for item in self.items[::-1]))

