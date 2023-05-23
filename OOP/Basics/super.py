class Class():
    def __init__(self, x):
        print(x)
  
# this is the subclass of class "Class"
class SubClass(Class):
    # def __init__(self, x):
  
    #     # this is how we call super
    #     # class's constructor
    #     super().__init__(x)
    def temp(self):
        pass

x = [1, 2, 3, 4, 5]
a = SubClass(x)

class Base():
    def __init__(self):
        print("Base Init")

class child1(Base):
    def __init__(self) -> None:
        super().__init__()
        print("child1 Init")

class mid(Base):
    def __init__(self):
        super().__init__()
        print("mid Init") 

class child2(Base):
    def __init__(self):
        super().__init__()
        print("child2 Init")

class child3(mid,child1,child2):
    def __init__(self) -> None:
        super().__init__()
        print("child3 Init")


ch3 = child3()
print(child3.__mro__)
print("#########################")



class Ten():
    def __init__(self,*args):
        print("Init TEN")
        self.args=args
    def adder(self):
        print("TEN ADDER")
        print(sum(self.args)+10)
        super().adder()
class Hundred():
    def __init__(self,*args) -> None:
        print("Init hundred")
        self.args=args
    def adder(self):
        print("HUNDRED ADDER")
        print(sum(self.args)+100)
class experiment(Ten,Hundred):
    pass

e = experiment(1,2,3)
e.adder()
print(experiment.__mro__)
print("#########################")

class Base():
    def __init__(self, reconnect=True, handle=None,
        interleaved=False, delay=20, interval=30, retries=20,
        dev_verification=True, **kwargs):
        
        self.retries = retries
        self.reconnect = reconnect
        self.delay = delay
        self.interval = interval
        self.handle = handle
        self.interleaved = interleaved
        self.dev_verification = dev_verification
        self.preVerify = kwargs.get('preVerify', False)
        self.postVerify = kwargs.get('postVerify', False)

    def launch(self):
        print("Preverify, PostVerify",self.preVerify, self.postVerify)

class Subclass(Base):
    def __init__(self, reconnect=True, handle=None,
        delay=20, interval=30, retries=20, interleaved=False, dev_verification=True, **kwargs):
        super().__init__(reconnect=reconnect, handle=handle,
            delay=delay, interval=interval, retries=retries, interleaved=interleaved, 
            dev_verification=dev_verification, **kwargs)

obj = Subclass(preVerify=True, postVerify=True)
obj.launch()
