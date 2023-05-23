# Inheritance provides a way to create a new class from an existing class. 
# The new class is a specialized version of the existing class such that it inherits all the public attributes (variables) and methods of the existing class. 
# The existing class is used as a starting point or base to create the new class.

from abc import abstractmethod

class Vehicle:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_name(self):
        print("Name:", self.name)
        print("Model:", self.model)


class FuelCar(Vehicle):

    def __init__(self, name, model, combust_type):
        Vehicle.__init__(self, name, model)
        self.combust_type = combust_type

    def get_fuel_car(self):
        super().get_name()
        print("Combust Type:", self.combust_type)

class GasolineCar(FuelCar):

    def __init__(self, name, model, combust_type, capacity):
        FuelCar.__init__(self, name, model, combust_type)
        self.capacity = capacity

    def get_gasoline_car(self):
        super().get_fuel_car()
        print("Capacity:", self.capacity)

class ElectricCar(Vehicle):

    def __init__(self, name, model, battery_power):
        Vehicle.__init__(self, name, model)
        self.battery_power = battery_power

    def get_electric_car(self):
        super().get_name()
        print("Battery Power:", self.battery_power)


class HybridCar(GasolineCar, ElectricCar):

    def __init__(self, name, model, combust_type, battery_power):
        FuelCar.__init__(self,name, model, combust_type)
        ElectricCar.__init__(self, name, model, battery_power)

    def get_hybrid_car(self):
        super().get_fuel_car()
        print("Battery Power:",self.battery_power)

# main
def main():
    print("Single inheritance:")
    Fuel = FuelCar("Honda", "Accord", "Petrol")
    Fuel.get_fuel_car()
    print("\n")

    print("Multi-level inheritance:")
    Fuel = GasolineCar("Toyota", "Corolla", "Gasoline","30 L")
    Fuel.get_gasoline_car()
    print("\n")

    print("Hierarchical inheritance:")
    Electric = ElectricCar("Tesla", "ModelX", "200MWH")
    Electric.get_electric_car()
    print("\n")

    print("Multiple inheritance:")
    Hybrid = HybridCar("Toyota", "Prius", "Hybrid", "100MWH")
    Hybrid.get_hybrid_car()



main()