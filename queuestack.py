from structures import Stack

class Queue():
    def __init__(self, size):
        self.size = size
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def enqueue(self, item):
        if len(self.stack1.list) < self.size:
            self.stack1.push(item)
    
    def dequeue(self):
        while self.stack1.list:
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()
        while self.stack2.list:
            self.stack1.push(self.stack2.pop())
    
    def display(self):
        print(self.stack1.list)
    
    def front(self):
        while self.stack1.list:
            self.stack2.push(self.stack1.pop())
        first = self.stack2.top()
        while self.stack2.list:
            self.stack1.push(self.stack2.pop())
        return first
    
    def isEmpty(self):
        if self.stack1.list:
            print("not empty")
        else:
            print("empty")

queue = Queue(5)

queue.isEmpty()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.display()
queue.dequeue()
queue.display()
print(queue.front())
queue.isEmpty()