class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

obj1=vehicle("250","90")
print(obj1.max_speed +" " + obj1.mileage)