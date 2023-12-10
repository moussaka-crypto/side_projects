class MiQueue:
    def __init__(self) -> None:
        self.items = []

    # FIFO
    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    # LIFO
    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop(-1)

    # PRIORITY QUEUE
    def pq_enqueue(self, x):
        self.items.append(x)
        self.items.sort(key=lambda x: x.value)
    