class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue:", ' '.join(map(str, self.queue)))

# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

print("Front item is:", q.peek())
