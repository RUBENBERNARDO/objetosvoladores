from abc import ABC, abstractmethod                                         #This method MUST to be imported because it is the way to create Abstrac Classes.
from enum import Enum                                                       #this method MUST to be imported too because it is the way to create Enum Classes.

def main():
    print("FLYING OBJECTS APP\n")

if __name__ == "__main__":
    main()

class VehicleState (Enum):                                                  #"Enum" indicates that VehicleState is an Enum Class.
    
    turned_on=1
    turned_off=2
    stoped=3
    traffic=4
    took_off=5

class Vehicle(ABC):                                                         #"ABC" indicates that Vehicle Class is an Abstrac Class.
    
    def __init__(self, fuel, wheel, capacity, state):
        self.fuel=""
        self.wheel=0
        self.capacity=0
        self.state=VehicleState

    @abstractmethod                                                         #"@abstracmethod" indicates that this method is an Abstrac Method.
    def _comunicate(self):
        pass                                                                #Use "pass" to leave the function of the method empty.

    @abstractmethod
    def _turn_on(self):                                                     #Use "_" to indicate that this method is private.
        pass

    @abstractmethod
    def _turn_off(self):
        pass

class IFlyingVehicle (Vehicle):

    @abstractmethod
    def lift_off(self):
        pass

    @abstractmethod
    def land(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

class Drone (IFlyingVehicle):

    def __init__(self) -> None:
        IFlyingVehicle().__init__()

class Airplane (IFlyingVehicle):

    def __init__(self, fuel, wheel, capacity, state):
        IFlyingVehicle().__init__(fuel, wheel, capacity, state)

class Helicopter (IFlyingVehicle):

    def __init__(self, fuel, wheel, capacity, state):
        super().__init__(fuel, wheel, capacity, state)



#############
drone1=Drone
drone1.fuel="Batteries"
drone1.wheel=0
drone1.capacity=2
drone1.state=VehicleState(2)
drone1._comunicate="I can comunicate with the controller signal"
drone1._turn_off=True

print(f"DEVICE: DRONE [1] \n Fuel type: {drone1.fuel} \n Number of wheels: {drone1.wheel} \n Actual state: {drone1.state} \n DRONE [1] message: {drone1._comunicate}\n")

#############
airplane1=Airplane
airplane1.fuel="Aviation fuel"
airplane1.wheel=6
airplane1.capacity=400
airplane1.state=VehicleState(2)
airplane1._comunicate="I can comunicate with the Control Tower and Control Base."
airplane1._turn_off=True

print(f"DEVICE: AIRPLANE [1] \n Fuel type: {airplane1.fuel} \n Number of wheels: {airplane1.wheel} pairs\n Actual state: {airplane1.state} \n Capacity: {airplane1.capacity} seats \n AIRPLANE [1] message: {airplane1._comunicate}\n")

#############
helicopter1=Helicopter
helicopter1.fuel="Aviation kerosene"
helicopter1.wheel=4
helicopter1.capacity=6
helicopter1.state=VehicleState(2)
helicopter1._comunicate="I can comunicate with the Control Tower and Control Base."
helicopter1._turn_off=True

print(f"DEVICE: HELICOPTER [1] \n Fuel type: {helicopter1.fuel} \n Number of wheels: {helicopter1.wheel} pairs \n Actual state: {helicopter1.state} \n Capacity: {helicopter1.capacity} seats \n HELICOPTER [1] message: {helicopter1._comunicate}\n")