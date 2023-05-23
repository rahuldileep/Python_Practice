class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,ndata):
        self.data=ndata
    def setnext(self,nnext):
        self.next=nnext
        
class Linked_List:
    def __init__(self):
        self.head=None
    def add_beg(self,data):
        Newnode=Node(data)
        if self.head==None:
            self.head=Newnode
        else:
            current=self.head
            self.head=Newnode
            Newnode.setnext(current)
    def add_end(self,data):
        NewNode=Node(data)
        current=self.head
        while current.getnext()!=None:
            current=current.getnext()
        current.setnext(NewNode)
    def add_pos(self,data,pos):
        i=1
        current=self.head
        prev=None
        while i<pos:
            prev=current
            current=current.getnext()
            i+=1
        NewNode=Node(data)
        prev.setnext(NewNode)
        NewNode.setnext(current)
    def display(self):
        current=self.head
        while current!=None:
            print(current.getdata(),end='->')
            current=current.getnext()
        print("\n")
    def delete(self,data):
        current=self.head
        prev=None
        while current.getdata()!=data and current!=None:
            prev=current
            current=current.getnext()
        prev.setnext(current.getnext())
    def reverse(self):
        current=self.head
        prev=None
        while current!=None:
            Next=current.getnext()
            current.setnext(prev)
            prev=current
            current=Next
        self.head=prev
    def sort(self):
        self.head=self.sort_helper(self.head)
    def sort_helper(self,head):
        if head is None or head.getnext() is None:
            return head
        l1, l2 = self.dividelist(head)
        l1=self.sort_helper(l1)
        l2=self.sort_helper(l2)
        head=self.merge(l1,l2)
        return head
        
    def dividelist(self, head):
        slow=head
        fast=head
        if fast:
            fast=fast.getnext()
        while fast:
            fast=fast.getnext()
            if fast:
                fast=fast.getnext()
                slow=slow.getnext()
        mid=slow.getnext()
        slow.setnext(None)
        return head, mid
    def merge(self,l1,l2):
        c1=c2=i=j=0
        cl1=l1
        cl2=l2
        while cl1!=None:
            c1+=1
            cl1=cl1.getnext()
        while cl2!=None:
            c2+=1
            cl2=cl2.getnext()
        temp=Node(0)
        dummy=temp
        while i<c1 and j<c2:
            if l1.getdata()<l2.getdata():
                temp.setnext(l1)
                l1=l1.getnext()
                i+=1
            else:
                temp.setnext(l2)
                l2=l2.getnext()
                j+=1
            temp=temp.getnext()
        while i<c1:
            temp.setnext(l1)
            l1 = l1.getnext()
            i += 1
            temp=temp.getnext()
        while j<c2:
            temp.setnext(l2)
            l2 = l2.getnext()
            j += 1
            temp=temp.getnext()
        temp.setnext(None)
        return dummy.getnext()

    """def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        temp=None
        if l1.getdata() < l2.getdata():
            temp=l1
            temp.setnext(self.merge(l1.getnext(),l2))
        else:
            temp=l2
            temp.setnext(self.merge(l1, l2.getnext()))
        return temp"""

L=Linked_List()
L.add_beg(10)
L.add_end(20)
L.add_end(30)
L.add_end(50)
L.add_end(60)
L.add_end(70)
L.add_pos(40,4)
L.display()
L.delete(70)
L.reverse()
L.display()
L.sort()
L.display()