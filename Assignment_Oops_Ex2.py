# class vehicle:
#     pass

#Exercise 3
class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

bus=vehicle("school","180","12")
print("Vehicle Name:",bus.name,"Volvo speed:",bus.max_speed,"Mileage",bus.mileage)

#Exercise4
class Bus(vehicle):
    def seating_capacity(self,capacity):
        
        self.capacity = capacity
obj2=Bus("50")
obj2.print("The seating capacity of a bus is",Bus.vehicle.capacity,"passengers")