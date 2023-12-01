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
    
    # def __str__(self):
    #     items = []
    #     if self.count() > 0:
    #         i = self.front
    #         if i > self.back:
    #             items.extend(self.items[i:])
    #             i = 0
    #         items.extend(self.items[i:self.back + 1])

    #     item_strings = [str(edge.name) if isinstance(edge, Edge) else str(edge) for edge in items]
    #     return "Queue: Front [{}] Back".format(", ".join(item_strings))
    #     #return "Queue: Front [{}] Back".format(", ".join(str(x) for x in items))
    