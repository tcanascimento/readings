
class Stack:
    def __init__(self, maxsize):
        self.items = []
        self.maxSize = maxsize

    def is_empty(self):
        return self.items == []

    def empty(self):
        self.items.clear()

    def push(self, item):
        if self.full():
            raise OverflowError("Pilha cheia!")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        return self.items.pop()

    def show_top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.maxSize
