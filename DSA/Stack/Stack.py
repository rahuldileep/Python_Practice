class Stack():
    def __init__(self):
        self.items=[]
    def isempty(self):
        if self.items==[]:
            print('Stack Empty')
        else:
            print('Not Empty')
    def push(self,data):
        self.items.append(data)
        print('Added %d'%data)
    def pop(self):
        print('Removed:',self.items.pop())
    def top(self):
        l=len(self.items)
        print('Element at top is: ',self.items[l-1])
    def display(self):
        print('Stack:',self.items)
S=Stack()
S.isempty()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
S.display()
S.top()
S.pop()
S.display()
S.top()

