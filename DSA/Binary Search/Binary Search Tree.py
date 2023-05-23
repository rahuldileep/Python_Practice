
class BST_Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def setdata(self,n_data):
        self.data=n_data
    def setleft(self,n_left):
        self.left=n_left
    def setright(self,n_right):
        self.right=n_right

class Queue():
    def __init__(self):
        self.items=[]

    def put(self,data):
        self.items.insert(0,data)

    def get(self):
        return self.items.pop()

    def empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)



class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class BST():
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=BST_Node(data)
        else:
            self.insert_helper(self.root,data)
    def insert_helper(self,root,data):
        if data < root.getdata():
            if root.getleft() is None:
                root.setleft(BST_Node(data))
            else:
                self.insert_helper(root.getleft(),data)
        elif data > root.getdata():
            if root.getright() is None:
                root.setright(BST_Node(data))
            else:
                self.insert_helper(root.getright(),data)

    def preorder(self):
        if self.root is None:
            return
        print('Preorder Traversal:')
        self.preorder_helper(self.root)
        print ('\n')
    def preorder_helper(self,root):
        if root is None:
            return
        print(root.getdata(),end='->')
        self.preorder_helper(root.getleft())
        self.preorder_helper(root.getright())

    def postorder(self):
        if self.root is None:
            return
        print('Postorder Traversal:')
        self.postorder_helper(self.root)
        print ('\n')
    def postorder_helper(self,root):
        if root is not None:
            self.postorder_helper(root.getleft())
            self.postorder_helper(root.getright())
            print (root.getdata(),end='->')

    def Inorder(self):
        if self.root is None:
            return
        print('Inorder Traversal:')
        self.Inorder_helper(self.root)
        print ('\n')
    def Inorder_helper(self,root):
        if root is not None:
            self.Inorder_helper(root.getleft())
            print (root.getdata(),end='->')
            self.Inorder_helper(root.getright())

    def levelorder(self):
        if self.root is not None:
            self.levelorder_helper(self.root)

    def levelorder_helper(self, root):
        result = []
        node = None
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            result.append(str(node.getdata()))
            if node.getleft() is not None:
                q.put(node.getleft())
            if node.getright() is not None:
                q.put(node.getright())
        print ('->'.join(result))

    def find(self,data):
        if self.root is None:
            return
        self.find_helper(self.root,data)
    def find_helper(self,root,data):
        if root.getdata()==data:
            print('Found:',data)
        elif root.getdata()<data:
            self.find_helper(root.getright(),data)
        else:
            self.find_helper(root.getleft(),data)
    def findmin(self):
        if self.root is None:
            return
        print('mINIMUM:',self.findmin_helper(self.root))
    def findmin_helper(self,root):
        current=root
        while current.getleft()!=None:
            current=current.getleft()
        return current.getdata()
    def findmax(self):
        if self.root is None:
            return
        print('Maximum:',self.findmax_helper(self.root))
    def findmax_helper(self,root):
        current=root
        while current.getright()!=None:
            current=current.getright()
        return current.getdata()

    def Successor(self,data):
        if self.root is None:
            return
        current=self.root
        node=None
        while current!=None:
            if current.getdata()==data:
                node=current
                break
            else:
                if current.getdata()<data:
                    current=current.getright()
                else:
                    current=current.getleft()
        ancestor = self.root
        successor=None
        if node is None:
            return
        if node.getright()!=None:
            temp=node.getright()
            while temp.getleft()!=None:
                temp=temp.getleft()
            successor=temp
        else:
            while ancestor!=node:
                if node.getdata() < ancestor.getdata():
                    successor=ancestor
                    ancestor=ancestor.getleft()
                else:
                    ancestor=ancestor.getright()
        print('Successor:',successor.getdata())

    def Predecessor(self,data):
        if self.root is None:
            return
        current=self.root
        node=None
        while current!=None:
            if current.getdata()==data:
                node=current
                break
            else:
                if current.getdata()<data:
                    current=current.getright()
                else:
                    current=current.getleft()
        ancestor=self.root
        predecessor=None
        if node.getleft()!=None:
            temp=node.getleft()
            while temp!=None:
                temp=temp.getright()
            predecessor=temp
        else:
            while ancestor!=node:
                if node.getdata()>ancestor.getdata():
                    predecessor=ancestor
                    ancestor=ancestor.getright()
                else:
                    ancestor=ancestor.getleft()
        print('Predecessor:',predecessor.getdata())

    def delete(self,data):
        if self.root is None:
            return False
        elif self.root.getdata() == data:
            if self.root.getleft() is None and self.root.getright() is None:
                self.root=None
            elif self.root.getleft() and self.root.getright() is None:
                self.root=self.root.getleft()
            elif self.root.getright() and self.root.getleft() is None:
                self.root=self.root.getright()
            elif self.root.getleft() and self.root.getright():
                parent=self.root
                delnode =self.root.getright()
                while delnode .getleft():
                    parent=delnode
                    delnode =delnode .getleft()
                self.root.setdata(delnode .getdata())
                if delnode .getright():
                    if parent.getdata() > delnode .getdata():
                        parent.setleft(delnode .getright())
                    elif delnode .getdata() < parent.getdata():
                        parent.setright(delnode .getright())
                else:
                    if delnode .getdata() < parent.getdata():
                        parent.setleft(None)
                    else:
                        parent.setright(None)
            return True
        parent=None
        node=self.root
        while node and node.getdata()!=data:
            parent=node
            if node.getdata() < data:
                node=node.getright()
            elif node.getdata() > data:
                node=node.getleft()
        if node is None and node.getdata()!=data:
            return False
        elif node.getleft() is None and node.getright() is None:
            if parent.getdata()>data:
                parent.setleft(None)
            else:
                parent.setright(None)
            return True
        elif node.getleft() and node.getright() is None:
            if data<parent.getdata():
                parent.setleft(node.getleft())
            else:
                parent.setright(node.getleft())
            return True
        elif node.getright() and node.getleft() is None:
            if data<parent.getdata():
                parent.setleft(node.getright())
            else:
                parent.setright(node.getright())
            return True
        else:
            parent=node
            delnode = node.getright()
            while delnode.getleft():
                parent=delnode
                delnode =delnode.getleft()
            node.setdata(delnode.getdata())
            if delnode.getright():
                if delnode.getdata() < parent.getdata():
                    parent.setleft(delnode.getright())
                elif delnode.getdata() > parent.getdata():
                    parent.setright(delnode.getright())
            else:
                if delnode.getdata() < parent.getdata():
                    parent.setleft(None)
                else:
                    parent.setright(None)
    def findsize(self):
        if self.root is None:
            return
        print('Size:',self.findsize_helper(self.root))
    def findsize_helper(self,root):
        if root is None:
            return 0
        return self.findsize_helper(root.getleft()) + self.findsize_helper(root.getright())+1
    def findsize_nonrecursive(self):
        if self.root is not None:
            self.findsize_nonrecursive_helper(self.root)
    def findsize_nonrecursive_helper(self,root):
        if root is None:
            return 0
        q=Queue()
        q.put(root)
        node=None
        count=0
        while not q.empty():
            node=q.get()
            count+=1
            if node.getleft():
                q.put(node.getleft())
            if node.getright():
                q.put(node.getright())
        print('Size using non recursive method:',count)
    def height(self):
        if self.root is not None:
            print('Height:',self.height_helper(self.root))
            self.height_nonrecursive(self.root)
    def height_helper(self,root):
        if root is None:
            return 0
        return max(self.height_helper(root.getleft()),self.height_helper(root.getright())) + 1
    def height_nonrecursive(self,root):
        q=Stack()
        q.push([root,1])
        temp=0
        while not q.empty():
            node, depth = q.pop()
            temp=max(temp,depth)
            if node.getleft():
                q.push([node.getleft(),depth+1])
            if node.getright():
                q.push([node.getright(),depth+1])

        print('Height using non recursive method:',temp)

    def deepestnode(self):
        if self.root is not None:
            self.deepestnode_helper(self.root)
    def deepestnode_helper(self,root):
        if root is None:
            return 0
        q=Queue()
        node = None
        q.put(root)
        while not q.empty():
            node=q.get()
            if node.getleft() is not None:
                q.put(node.getleft())
            if node.getright() is not None:
                q.put(node.getright())
        print('Deepest Node:',node.getdata())
    def leafcount(self):
        if self.root is not None:
            self.leafcount_helper(self.root)
    def leafcount_helper(self,root):
        q=Queue()
        count=0
        q.put(root)
        node=None
        while not q.empty():
            node=q.get()
            if node.getright() is None and node.getleft() is None:
                count+=1
            if node.getleft():
                q.put(node.getleft())
            if node.getright():
                q.put(node.getright())
        print('Number of leaf nodes:',count)
    def reverse_levelorder_display(self):
        if self.root is not None:
            print('Reversed Level Order Display:')
            self.reverse_levelorder_display_helper(self.root)
            print('\n')

    def reverse_levelorder_display_helper(self,root):
        if root is not None:
            q=Queue()
            s=Stack()
            node=None
            q.put(root)
            while not q.empty():
                node=q.get()
                if node.getleft() is not None:
                    q.put(node.getleft())
                if node.getright() is not None:
                    q.put(node.getright())
                s.push(node.getdata())
        while (not s.empty()):
            print(s.pop(),end='->')
        print('\n')
bst=BST()
bst.insert(12)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(13)
bst.insert(17)
bst.insert(19)
bst.insert(25)
bst.insert(23)
bst.insert(50)
bst.insert(100)
bst.preorder()
bst.Inorder()
bst.postorder()
bst.levelorder()
bst.find(9)
bst.findmin()
bst.findmax()
bst.Successor(9)
bst.Predecessor(13)
bst.delete(25)
bst.Inorder()
bst.findsize()
bst.findsize_nonrecursive()
bst.height()
bst.Inorder()
bst.deepestnode()
bst.leafcount()
bst.reverse_levelorder_display()