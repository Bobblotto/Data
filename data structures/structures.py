
class Stack(): # LIFO

    def __init__(self, size):
        self.size = size
        self.list = []
    
    def push(self, item):
        if len(self.list) < self.size:
            self.list.append(item)
        else:
            print("list full")
    
    def pop(self):
        if self.list != []:
            return self.list.pop(-1)
    
    def top(self):
        if self.list != []:
            return self.list[-1]

    def display(self):
        print(self.list)

"""stack = Stack(5)
stack.display()

stack.push("daniel")
stack.display()
stack.push("rose")
stack.display()
stack.push("ben")
stack.display()
stack.push("lara")
stack.display()
stack.push("isaac")
stack.display()

stack.push("chloe")
stack.display()

stack.pop()
stack.display()

print(stack.top())"""

class Queue(): # FIFO

    def __init__(self, size):
        self.size = size
        self.list = []
    
    def enqueue(self, item):
        if len(self.list) < self.size:
            self.list.append(item)
        else:
            print("list full")
    
    def dequeue(self):
        if self.list != []:
            self.list.pop(0)
    
    def front(self):
        if self.list != []:
            return self.list[0]

    def display(self):
        print(self.list)

"""queue = Queue(5)

queue.enqueue("jared")
queue.display()
queue.enqueue("dan")
queue.enqueue("ella")
queue.display()
print(queue.front())
queue.dequeue()
queue.display()

from collections import deque
queue2 = deque()

print(queue2)
print(type(queue2)) # check data type
queue2.append("tom")
print(queue2)
queue2.append("sasha")
print(queue2)
queue2.remove(queue2[0])
print(queue2)"""

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def addChild(self, node):
        self.children.append(node)
    
    def display(self, index):
        print("  "*index, "|__", self.data)
        
        if self.children:
            for child in self.children:
                child.display(index+1)
                


electronics = Node("Electronics")

phone = Node("Phone")
tv = Node("TV")
laptop = Node("Laptop")

electronics.addChild(phone)
electronics.addChild(tv)
electronics.addChild(laptop)

android = Node("Android")
apple = Node("iOS")
intel = Node("Intel")

phone.addChild(android)
phone.addChild(apple)
phone.addChild(intel)

lenovo = Node("Lenovo")

laptop.addChild(lenovo)

electronics.display(0)
