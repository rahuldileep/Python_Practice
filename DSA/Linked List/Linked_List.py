#!/usr/bin/env python3

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None:
            print("Empty List")
        else:
            current = self.head
            while current:
                print(current.val,end="->")
                current = current.next
            print("\n===========================")
    def add(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def remove(self,val):
        if val == self.head.val:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current:
            if val == current.val:
                prev.next = current.next
                print("Removed:%d"%(val))
                return
            prev = current
            current = current.next
        print("Value not found")
    def reverse(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

obj1 = LinkedList()
obj1.display()
obj1.add(10)
obj1.add(100)
obj1.add(1000)
obj1.add(10000)
obj1.display()
obj1.remove(100)
obj1.display()
obj1.add(100000)
obj1.reverse()
obj1.display()