class Queue:

    def __init__(self):
        self.elements = []

    # FIFO (Queue)
    def enqueue(self, data):
        self.elements.append(data)

    def dequeue(self):
        return self.elements.pop(0)

    # LIFO (Stack)
    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop(-1)

    # PRIO Queue
    def prio_enqueue(self, data):
        self.elements.append(data)
        self.elements.sort(key=lambda x: x.value)

    def is_empty(self):
        return len(self.elements) == 0
