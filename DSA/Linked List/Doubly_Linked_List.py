#!/usr/bin/env python3

class Node():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Doubly_Linked_List():
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None:
            print("Empty List")
        else:
            print("================================")
            current = self.head
            while current:
                print(current.val,end="->")
                current = current.next
            print("\n================================")
    
    def add(self, val):
        print("Adding Value: ",val)
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
    
    def remove(self, val):
        print("Removing Value: ",val)
        if self.head.val == val:
            self.head = self.head.next
        current = self.head
        prev = None
        while current.next:
            if current.val == val:
                current.next.prev = prev
                prev.next = current.next
                return
            else:
                prev = current
                current = current.next
        if current.val == val:
            prev.next = None

    def reverse(self):
        if not self.head:
            print("Empty List")
            return
        current = self.head
        prev = None
        while current:
            temp_next = current.next
            current.next = prev
            prev = current
            current.prev = temp_next
            current = temp_next
        self.head = prev

obj1 = Doubly_Linked_List()
obj1.display()
obj1.add(10)
obj1.add(100)
obj1.add(1000)
obj1.add(10000)
obj1.add(100000)
obj1.display()
obj1.remove(100000)
obj1.display()
obj1.add(100000)
obj1.reverse()
obj1.display()