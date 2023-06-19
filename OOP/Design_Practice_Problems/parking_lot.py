# 1.Requirements
# 1.1 - Multi level parking with a capacity of 10,000
# 1.2 - Different types of parking spots. Compact, Large, Handicapped, Motorcycle.
# 1.3 - Multiple entrances and multiple exit points.
# 1.4 - A ticket gets issued at the entrance and validation/payment happens at exit.
# 1.5 - Rate should be calculated hourly. Option to pay with credit card and Cash.
# 1.6 - Display board at the entrance to show the number of free spots.

# 2.Identify the main Actors
# 2.1 - Customer -  The customer can park at an empty spot and pay for it while exiting.
# 2.2 - Admin - Responsible for adding/removing the parking spot & entrance/exit points.
# 2.2 - System - Responsible for alloting a parking spot & show details on current availability.

# 3. Usecases for each actor
# 3.1 - Customer
#  - Take Ticket
#  - Scan Ticket
#  - Pay Ticket
#  - Park Vehicle
# 3.2 - Admin 
#  - Add parking spot
#  - Remove Parking spot
#  - Add entry point
#  - Add exit point
# 3.3 - System
#  - Display availability
#  - Assigning availble spots to vehicle

# 4. Identify extend and include relationships
# 4.1 - Scan ticket usecase has an include relationship with pay Ticket

# 5.Identify the components/classes of the system
#  - Vehicle - CompactVehicle, LargeVehicle, Motorcycle
#  - ParkingSpot - CompactSpot, LargeSpot, HandicappedSpot, MotorcycleSpot
#  - ParkingTicket
#  - Entry
#  - Exit
#  - Display
#  - ParkingLevel
#  - ParkingLot
#  - Payment

# 6. Relationships between classes
# 6.1 - Association
#  - ParkingSpot class has a one-way association with Vehicle
#  - Vehicle, Entrance, Exit has one-way association with ParkingTicket
#  - The Payment has a two-way association with ParkingTicket
# 6.2 - Composition
#  - ParkingLot includes ParkingSpot, ParkingLevel, Display, Entry, Exit, ParkingTicket
# 6.3 - Inheritance
#  - CompactSpot, LargeSpot, HandicappedSpot, MotorcycleSpot inherits ParkingSpot

# 7. Class Diagram

# 8. Design Pattern
# 8.1 - Singleton Pattern - Only single instance of ParkingLot class
# 8.2 - Abstract Factory & Factory - ParkingLot is composed of smaller components which needs to be instantiated.

# 9. Enums
# 9.1 - TicketStatus
# 9.2 - VehicleType
# 9.3 - SpotType

# 10. Code

from abc import ABC, abstractmethod
from enum import Enum
import time

class TicketStatus(Enum):
	ACTIVE = 1
	COMPLETE = 2

class VehicleType(Enum):
	COMPACT = "compact"
	LARGE = "large"
	MOTORCYCLE = "motorcycle"
	HANDICAPPED = "handicapped"

class SpotType(Enum):
	FREE = 1
	TAKEN = 2

class ParkingSpot(ABC):

	def __init__(self):
		self._id = self.generateID()

	def generateID(self) :
		return str(time.time()).split('.')[0]
		

class CompactSpot(ParkingSpot):
	def __init__(self):
		super().__init__()

class LargeSpot(ParkingSpot):
	def __init__(self):
		super().__init__()

class HandicappedSpot(ParkingSpot):
	def __init__(self):
		super().__init__()

class MotorcycleSpot(ParkingSpot):
	def __init__(self):
		super().__init__()

class Vehicle(ABC):

	def __init__(self, license_plate):
		self.license_plate = license_plate

class CompactVehicle(Vehicle):
	def __init__(self, license_plate):
		super().__init__(license_plate)
		self.vehicle_type = VehicleType.COMPACT

class LargeVehicle(Vehicle):
	def __init__(self, license_plate):
		super().__init__(license_plate)
		self.vehicle_type = VehicleType.LARGE

class Motorcycle(Vehicle):
	def __init__(self, license_plate):
		super().__init__(license_plate)
		self.vehicle_type = VehicleType.MOTORCYCLE

class HandicappedVehicle(Vehicle):
	def __init__(self, license_plate):
		super().__init__(license_plate)
		self.vehicle_type = VehicleType.HANDICAPPED

class Entrance:
	def __init__(self):
		self.__id = self.generateID()
	def get_ticket(self, vehicle):
		return Ticket(vehicle)
	def generateID(self) :
		return str(time.time()).split('.')[0]


class Exit:
	def __init__(self):
		self.__id = self.generateID()
	def validate_ticket(self, ticket):
		pass
	def generateID(self) :
		return str(time.time()).split('.')[0]

class Ticket :
	def __init__(self, vehicle) :
		self.vehicle = vehicle
		self.status  = TicketStatus.ACTIVE
		self.inTime  = time.time()
		self.outTime = None
		self.payment = None
		self.spot    = None	
	def generateID(self) :
		yield range(1,1000)

class ParkingLot:
	def __init__(self, name, address):
		self._name = name
		self._address = address
		self.levels = []
		self._entrances = []
		self._exits = []

	def add_entrance(self, entrance):
		self._entrances.append(entrance)

	def add_exit(self, exit):
		self._exits.append(exit)

	def add_level(self, level):
		self.levels.append(level)

	def process_entry(self, ticket):
		for level in self.levels:
			if level.spots[ticket.vehicle.vehicle_type][SpotType.FREE]:
				ticket.spot = level.assign_spot(ticket)
				print(f"Spot assigned for {ticket.vehicle.license_plate}")
				break
	
	def process_exit(self, ticket):
		for level in self.levels:
			if ticket.spot in level.spots[ticket.vehicle.vehicle_type][SpotType.TAKEN]:
				level.unassign_spot(ticket)
				break
		ticket.spot = None
		ticket.outTime = time.time()
		ticket.status = TicketStatus.COMPLETE
		ticket.payment = Payment(ticket.inTime, ticket.outTime)
		print(f"Total amount for {ticket.vehicle.license_plate}: ${ticket.payment.amount}\n")
		
class ParkingLevel:
	def __init__(self, name):
		self.name = name
		self.spots = {
			VehicleType.COMPACT : {
				SpotType.FREE: [],
				SpotType.TAKEN: []
			  },
			  VehicleType.LARGE : {
				SpotType.FREE: [],
				SpotType.TAKEN: []
			  },
			  VehicleType.MOTORCYCLE : {
				SpotType.FREE: [],
				SpotType.TAKEN: []
			  },
			  VehicleType.HANDICAPPED : {
				SpotType.FREE: [],
				SpotType.TAKEN: []
			  }
			}

	def add_spots(self, spot_type, count):
		for _ in range(count):
			if spot_type == VehicleType.COMPACT:
				spot = CompactSpot()
			elif spot_type == VehicleType.LARGE:
				spot = LargeSpot()
			elif spot_type == VehicleType.MOTORCYCLE:
				spot = MotorcycleSpot()
			else:
				spot = HandicappedSpot()
			self.spots[spot_type][SpotType.FREE].append(spot)
			
	def assign_spot(self, ticket):
		spot = self.spots[ticket.vehicle.vehicle_type][SpotType.FREE].pop()
		ticket.spot = spot
		self.spots[ticket.vehicle.vehicle_type][SpotType.TAKEN].append(spot)
		return ticket.spot

	def unassign_spot(self, ticket):
		self.spots[ticket.vehicle.vehicle_type][SpotType.TAKEN].remove(ticket.spot)
		self.spots[ticket.vehicle.vehicle_type][SpotType.FREE].append(ticket.spot)


class DisplayBoard:
	def __init__(self, parking_lot):
		self.__parking_lot = parking_lot
	
	def show(self):
		for level in self.__parking_lot.levels:
			print(f"\n{level.name} - Available spots\n")
			print(VehicleType.COMPACT.name, len(level.spots[VehicleType.COMPACT][SpotType.FREE]))
			print(VehicleType.LARGE.name, len(level.spots[VehicleType.LARGE][SpotType.FREE]))
			print(VehicleType.MOTORCYCLE.name, len(level.spots[VehicleType.MOTORCYCLE][SpotType.FREE]))
			print(VehicleType.HANDICAPPED.name, len(level.spots[VehicleType.HANDICAPPED][SpotType.FREE]))
		
class Payment:
	def __init__(self, in_time = 0, out_time = 0):
		self.__rate = 10
		self.amount = self.calc_total(in_time, out_time)
	def set_rate(self, rate):
		self.__rate = rate
	def get_rate(self):
		return self.__rate
	def calc_total(self, in_time, out_time):
		delta = out_time - in_time
		minutes, seconds = divmod(delta, 60)
		hours, minutes = divmod(minutes, 60)
		print(f"\nTotal time: {hours}:{minutes}:{seconds}")
		return self.get_rate()*hours 

parking_lot_obj = ParkingLot("North Zone", "Santa Clara")
parking_level_1_obj = ParkingLevel("Level-1")
parking_level_2_obj = ParkingLevel("Level-2")
parking_level_1_obj.add_spots(VehicleType.COMPACT,10)
parking_level_1_obj.add_spots(VehicleType.LARGE,10)
parking_level_1_obj.add_spots(VehicleType.MOTORCYCLE,5)
parking_level_1_obj.add_spots(VehicleType.HANDICAPPED,10)
parking_level_2_obj.add_spots(VehicleType.COMPACT,10)
parking_level_2_obj.add_spots(VehicleType.LARGE,10)
parking_level_2_obj.add_spots(VehicleType.MOTORCYCLE,5)
parking_level_2_obj.add_spots(VehicleType.HANDICAPPED,10)
entrance_1_obj = Entrance()
entrance_2_obj = Entrance()
exit_1_obj = Exit()
exit_2_obj = Exit()
parking_lot_obj.add_entrance(entrance_1_obj)
parking_lot_obj.add_entrance(entrance_2_obj)
parking_lot_obj.add_exit(exit_1_obj)
parking_lot_obj.add_exit(exit_2_obj)
parking_lot_obj.add_level(parking_level_1_obj)
parking_lot_obj.add_level(parking_level_2_obj)
Board = DisplayBoard(parking_lot_obj)
Board.show()
print("\n\n")
car = CompactVehicle("1234")
truck = LargeVehicle("5678")
van = HandicappedVehicle("1278")
bike = Motorcycle("9821")
car_ticket = entrance_1_obj.get_ticket(car)
parking_lot_obj.process_entry(car_ticket)
truck_ticket = entrance_1_obj.get_ticket(truck)
parking_lot_obj.process_entry(truck_ticket)
van_ticket = entrance_2_obj.get_ticket(van)
parking_lot_obj.process_entry(van_ticket)
bike_ticket = entrance_2_obj.get_ticket(bike)
parking_lot_obj.process_entry(bike_ticket)
Board.show()
time.sleep(4)
parking_lot_obj.process_exit(car_ticket)
parking_lot_obj.process_exit(bike_ticket)
Board.show()