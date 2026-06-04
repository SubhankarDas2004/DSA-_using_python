class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):

        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return


        if self.front == -1:
            self.front = 0


        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print("Enqueued:", data)

    def dequeue(self):
    
        if self.front == -1:
            print("Queue is Empty")
            return None

        data = self.queue[self.front]


        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print("Dequeued:", data)
        return data

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()

cq.dequeue()
cq.dequeue()
cq.display()

cq.enqueue(50)
cq.display()
