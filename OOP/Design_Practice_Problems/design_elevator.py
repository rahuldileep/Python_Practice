"""
1. Requirements
 - Building should have multiple elevators.
 - Button panel on every floor for calling the elevator.
 - Button panel with all floor options inside for the user to move to any desired floor.
 - Display on the inside and outside to show the current floor of the elevator.
 - Elevator system should have the algorithm to move the elevator based on FCFS.
 - Elevator can move in up/down direction and can be in idle state.

2. Identify the Actors
 - Passenger
 - System

3. Usecases
 - Passenger
   - Press elevatory panel button
   - Press floor panel button
 - System
   - Floor request 
   - Door open/close request
   - Move/Stop the elevator
   - Dispatcher ALgorithm
   - Open/Close Doors
   - Display inside/outside
   - Request for elevator
   - Call emergency

4. Identify extend and include relationship
 - Include
   - Floor request  has an include relationship with Move/Stop the elevator
   - Door open/close request has include relationship with Open/Close Doors
   - Press floor panel button has include relationship with Request for elevator

5. Identify the components/classes
 - Button - FloorButton & ElevatorButton
 - FloorPanel 
 - ElevatorPanel
 - Display
 - Door
 - Floor
 - Elevator 
 - Elevator System
 - Building

6. Relationships between classes
 - Aggregation 
   - The ElevatorSystem has an aggregation relationship with Building. 
 - Composition
   - Elevator is composed of Door, Display, Panel
   - Building is composed of ElevatorSystem and Floor
   - Floor is composed of FloorPanel and Display
   - FloorPanel is composed of the FloorButton.
   - ElevatorPanel is composed of the ElevatorButton.
 - Inhertance 
   - Button - FloorButton & ElevatorButton

7. Class Diagram

8. Design Pattern 
 - Strategy Pattern - system could have multiple dispatch request strategy classes.

9. Enums
 - ElevatorState
 - DoorState
 - Direction 

10.Code
"""
from enum import Enum
from abc import ABC, abstractmethod
import random
from heapq import heappush, heappop

class ElevatorState(Enum):
    IDLE = 1
    UP = 2
    DOWN = 3

class DoorState(Enum):
    OPEN = 1
    CLOSE = 2

class Direction(Enum):
    UP = 1
    DOWN = 2

class ButtonStatus(Enum): 
  PRESSED = 1
  UNPRESSED = 0

class RequestType(Enum):
    EXTERNAL = 1
    INTERNAL = 2

class Button(ABC):
    def __init__(self, status = ButtonStatus.UNPRESSED) -> None:
        self.status = status
    
    def is_pressed(self):
        self.status = ButtonStatus.PRESSED
        return self.send_request()

    def unpress(self):
        print("BUTTON UNPRESSED")
        self.status = ButtonStatus.UNPRESSED

    @abstractmethod
    def send_request(self):
        pass

class FloorButton(Button):
    def __init__(self, direction, floor_number) -> None:
        self.direction = direction
        self.floor_number = floor_number
    
    def send_request(self):
        print(f"Button pressed on floor {self.floor_number} panel.\nRequesting {self.direction.name} direction")
        print("Sending Request")
        if self.direction == Direction.UP:
            request = Request(RequestType.EXTERNAL, Direction.UP, self.floor_number, self.floor_number)
        else:
            request = Request(RequestType.EXTERNAL, Direction.DOWN, self.floor_number, self.floor_number)
        return request
    
class ElevatorButton(Button):
    def __init__(self, dest_floor, current_floor) -> None:
        self.dest_floor = dest_floor
        self.current_floor = current_floor

    def send_request(self):
        print(f"Button pressed on elevator panel.\nRequesting floor {self.dest_floor}")
        print("Sending Request")
        if self.dest_floor > self.current_floor:
            request = Request(RequestType.INTERNAL, Direction.UP, self.current_floor, self.dest_floor)
        else:
            request = Request(RequestType.INTERNAL, Direction.DOWN, self.current_floor, self.dest_floor)
        return request

class FloorPanel():
    def __init__(self, up_button, down_button) -> None:
        self.up_button = up_button
        self.down_button = down_button

class ElevatorPanel():
    def __init__(self, go_to_floor_buttons) -> None:
        self.go_to_floor_buttons = go_to_floor_buttons

class Floor:
    def __init__(self, floor_panel, display) -> None:
        self.display = display
        self.floor_panel = floor_panel

class Display:
    def __init__(self, floor, capacity, direction) -> None:
        self.floor = floor
        self.capacity = capacity
        self.direction = direction

    def show_elevator_display(self):
        print(f"Floor:{self.floor}")
        print(f"Capacity:{self.capacity}")

    def show_hall_display(self):
        print(f"Floor:{self.floor}")

class Door:
    def __init__(self, state) -> None:
        self.state = state
    
    def is_open(self):
        return self.state == DoorState.OPEN

class Elevator:
    def __init__(self, id, state, display, floors, door, current_floor) -> None:
        self.id  = id
        self.state = state
        self.display = display
        self.door = door
        self.current_floor = current_floor
        self.go_to_floor_buttons = [ElevatorButton(i,0) for i in range(floors)]
        self.panel = ElevatorPanel(self.go_to_floor_buttons)
        self.up_requests = []
        self.down_requests = []

    def move(self):
        print(f"Elevator {self.id} on floor {self.current_floor} moving in {self.state.name} direction")
      
    def stop(self):
        print(f"Elevator {self.id} stopped at {self.current_floor} floor")
    
    def open_door(self):
        print(f"Elevator {self.id} opening door")
        self.door = DoorState.OPEN
    
    def close_door(self):
        print(f"Elevator {self.id} closing door")
        self.door = DoorState.CLOSE

    def process_request(self, request):
        if request.direction == Direction.UP:
            heappush(self.up_requests,(abs(self.current_floor - request.dest_floor), request))
        else:
            heappush(self.down_requests,(abs(self.current_floor - request.dest_floor), request))
        if self.up_requests:
            self.process_up_request()
            self.process_down_request()
        else:
            self.process_down_request()

    def process_up_request(self):
        while self.up_requests:
            current_request = self.up_requests.pop(0)[1]
            self.state = ElevatorState.UP
            self.close_door()
            self.move()
            self.current_floor = current_request.dest_floor
            self.stop()
            self.open_door()
            if current_request.dest_floor == current_request.source_floor:
                print(f"Picking up people at floor{self.current_floor}")
            else:
                print(f"Droppping peole at {self.current_floor}")
            self.close_door()
        self.state = ElevatorState.IDLE
    
    def process_down_request(self):
        while self.down_requests:
            current_request = self.down_requests.pop(0)[1]
            if self.current_floor > current_request.dest_floor:
                self.state = ElevatorState.DOWN
            else:
                self.state = ElevatorState.UP
            self.move()
            self.current_floor = current_request.dest_floor
            self.stop()
            self.open_door()
            if current_request.dest_floor == current_request.source_floor:
                print(f"Picking up people at {self.current_floor}")
            else:
                print(f"Droppping people at {self.current_floor}")
            self.close_door()
        self.state = ElevatorState.IDLE
    
class ElevatorSystem:
    def __init__(self, building) -> None:
        self.building = building
        self.requests = []

    def monitoring(self):
        pass

    def dispatch(self):
        floor = random.choice(self.building.floors)
        request1 = floor.floor_panel.down_button.is_pressed()
        elevator1 = self.building.elevators.pop(0)
        elevator1.process_request(request1)
        # elevator2 = self.building.elevators.pop(0)
        request2 = elevator1.panel.go_to_floor_buttons[-1].is_pressed()
        elevator1.process_request(request2)

class Building:
    _capacity = 10
    def __init__(self, floor_count, elevator_count) -> None:
        self.floor_count = floor_count
        self.elevators = []
        self.floors = []
        self.go_to_floor_buttons = []
        self.add_floors(floor_count)
        self.add_elevators(elevator_count)
        
    def add_floors(self, count):
        for floor in range(count):
            up_button = FloorButton(Direction.UP, floor)
            down_button = FloorButton(Direction.DOWN, floor)
            floor_panel = FloorPanel(up_button, down_button)
            floor_display = Display(floor, self._capacity,Direction.UP)
            self.floors.append(Floor(floor_panel, floor_display))

    def add_elevators(self, count):
        for elevator in range(count):
            display = Display(0,10,Direction.UP)
            door = Door(DoorState.OPEN)
            self.elevators.append(Elevator(elevator, ElevatorState.IDLE, display, self.floor_count, door, 0))
    
class Request:
    def __init__(self, req_type, direction, source_floor, dest_floor) -> None:
        self.req_type = req_type
        self.direction = direction
        self.source_floor = source_floor
        self.dest_floor = dest_floor

    

Building_obj = Building(10, 2)
elevator_system_obj = ElevatorSystem(Building_obj)
elevator_system_obj.dispatch()