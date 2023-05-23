class Queue():
    def __init__(self):
        self.items=[]
    def isempty(self):
        if self.items==[]:
            print('Queue Empty')
        else:
            print('Not Empty')
    def enqueue(self,data):
        self.items.insert(0,data)
        print('Added %d'%data)
    def dequeue(self):
        print('Removed:',self.items.pop())
    def display(self):
        print('Queue:',self.items)
    def peek(self):
        l=len(self.items)
        print('First Element is:',self.items[l-1])
Q=Queue()
Q.isempty()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
Q.display()
Q.peek()
Q.dequeue()
Q.display()
Q.peek()
