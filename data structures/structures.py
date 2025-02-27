from collections import deque

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
                


"""electronics = Node("Electronics")

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

electronics.display(0)"""

class NodeBin():

    def __init__(self, data):
        self.data = data

        self.leftChild = None
        self.rightChild = None
    
    def addChild(self, num):

        if num < self.data:
            if not self.leftChild:
                node = NodeBin(num)
                self.leftChild = node
            else:
                self.leftChild.addChild(num)
        elif num > self.data:
            if not self.rightChild:
                node = NodeBin(num)
                self.rightChild = node
            else:
                self.rightChild.addChild(num)
        else:
            print("Error: Value already in tree")
    
    def display(self, index):
        print("  "*index, "|__", self.data)
        
        if self.leftChild:
            self.leftChild.display(index+1)
        if self.rightChild:
            self.rightChild.display(index+1)
    
    def inOrder(self):
        
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.data)
        if self.rightChild:
            self.rightChild.inOrder()
    
    def preOrder(self):

        print(self.data)
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

    def delete(self, num):

        if num < self.data:

            if self.leftChild:
                if self.leftChild.data == num:
                    if not self.leftChild.leftChild and not self.leftChild.rightChild:
                        self.leftChild = None
                    elif self.leftChild.leftChild and not self.leftChild.rightChild:
                        self.leftChild.data = self.leftChild.leftChild.data
                    elif not self.leftChild.leftChild and self.leftChild.rightChild:
                        self.leftChild.data = self.leftChild.rightChild.data
                        self.leftChild.rightChild = None
                    elif self.leftChild.leftChild and self.leftChild.rightChild:
                        pass
                else:
                    self.leftChild.delete(num)
        elif num > self.data:

            if self.rightChild:
                if self.rightChild.data == num:
                    if not self.rightChild.leftChild and not self.rightChild.rightChild:
                        self.rightChild = None
                    elif self.rightChild.leftChild and not self.rightChild.rightChild:
                        self.rightChild.data = self.rightChild.leftChild.data
                        self.rightChild.leftChild = None
                    elif not self.rightChild.leftChild and self.rightChild.rightChild:
                        self.rightChild.data = self.rightChild.rightChild.data
                        self.rightChild.rightChild = None
                    elif self.rightChild.leftChild and self.rightChild.rightChild:
                        self.rightChild.data = self.rightChild.min2().data
                        self.rightChild.leftChild = None
                        self.rightChild.rightChild = None
                       # self.rightChild.min2() = None
                        #self.rightChild.delete(self.rightChild.min2().data)
                else:
                    self.rightChild.delete(num)

    def delete2(self, num):

        if num < self.data:

            if self.leftChild:
                self.leftChild = self.leftChild.delete2(num)
        elif num > self.data:

            if self.rightChild:
                self.rightChild = self.rightChild.delete2(num)
        else:

            if not self.leftChild and not self.rightChild:
                return None
            elif not self.rightChild:
                return self.leftChild
            elif not self.leftChild:
                return self.rightChild
            else:
                min = self.rightChild.min2()
                self.data = min.data

                self.rightChild = self.rightChild.delete2(min.data)

        return self
            
            
    def min2(self):

        if self.leftChild:
            return self.leftChild.min2()
        else:
            return self

    def minMax(self):

        print(self.min())
        print(self.max())
    
    def min(self):

        if self.leftChild:
            return self.leftChild.min()
        else:
            return "min", self.data
    
    def max(self):

        if self.rightChild:
            return self.rightChild.max()
        else:
            return "max", self.data

    def MM(self):

        min = self
        max = self

        while min.leftChild:
            min = min.leftChild
        print("min: ", min.data)

        while max.rightChild:
            max = max.rightChild
        print("max: ", max.data)

"""node = NodeBin(10)

node.addChild(7)
node.addChild(6)
node.addChild(12)
node.addChild(11)
node.addChild(13)

node.inOrder()
print("------------------------")

node.delete2(12)

node.inOrder()
node.minMax()"""

dic = { # graph
    "a" : ["b", "c", "d"],
    "b" : ["a", "d"],
    "c" : ["a", "d", "e"],
    "d" : ["a", "b", "c", "e"],
    "e" : ["c", "d"]
}

def breadthFastSearch(dic, start):

    visited = []

    queue = deque([start])
    visited.append(start)

    while queue:
        front = queue.popleft()
        print(front)
        for item in dic[front]:
            if item not in visited:
                queue.append(item)
                visited.append(item)

breadthFastSearch(dic, "a")

print("-----------------------------------")

def depthFastSearch(dic, start):

    visited = []

    stack = [start]
    visited.append(start)

    while stack:
        last = stack.pop()
        print(last)
        for item in dic[last]:
            if item not in visited:
                stack.append(item)
                visited.append(item)

depthFastSearch(dic, "a")

                visited.append(item)

breadthFastSearch(dic, "a")
