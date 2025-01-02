
class Stack():

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
            self.list.pop(-1)
    
    def top(self):
        if self.list != []:
            print(self.list[-1])


    def display(self):
        print(self.list)

stack = Stack(5)
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

stack.top()