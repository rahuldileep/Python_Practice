from abc import ABC, abstractmethod
class abs_Dept(ABC):
    @abstractmethod
    def __init__(self,employees):
        pass
    @abstractmethod
    def printemployees(self):
        pass


class Department(abs_Dept):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self._dpts = []
    def add(self,dept):
        self._dpts.append(dept)
        self.employees += dept.employees
    def printemployees(self):
        print("Parent Dept:",self.base_employees)
        for dept in self._dpts:
            dept.printemployees()
        print("Total employees:",self.employees)


class Test(abs_Dept):
    def __init__(self,employees):
        self.employees = employees
    def printemployees(self):
        print("Test:",self.employees)

class Development(abs_Dept):
    def __init__(self,employees):
        self.employees = employees
    def printemployees(self):
        print("Dev:",self.employees)


test = Test(100)
dev = Development(200)
Parent = Department(50)
Parent.add(test)
Parent.add(dev)
Parent.printemployees()

print("#"*40)

class MenuComponent(ABC):
    def __init__(self,menuitem) -> None:
        self.menuitem = menuitem

    @abstractmethod
    def add(self):
        pass

class MenuItem(MenuComponent):
    def __init__(self, menuitem) -> None:
        super().__init__(menuitem)
    
    def printmenu(self):
        print(self.menuitem)

    def add(self):
        pass

class Menu(MenuComponent):
    def __init__(self, name) -> None:
        self.components = []
        super().__init__(name)
    
    def printmenu(self):
        for comp in self.components:
            if isinstance(comp,Menu):
                print("%s>>"%(comp.menuitem))
            comp.printmenu()

    def add(self, menuitem):
        self.components.append(menuitem)

file = Menu("File")
file.add(MenuItem("New"))
file.add(MenuItem("Open"))
file.add(MenuItem("Close"))
recent_files = Menu("recent")
file.components.append(recent_files)
recent_files.add(MenuItem("file1.txt"))
recent_files.add(MenuItem("file2.txt"))
recent_files.add(MenuItem("file3.txt"))
file.printmenu()