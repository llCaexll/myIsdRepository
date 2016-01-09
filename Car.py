class Car:
    _manufacturer=""
    _brand=""
    _maxSpeed=100
    _driving=False
    _mileage=12.0
    
    def __init__(self):
        _manufacturer=""
        _brand=""
        _maxSpeed=100
        _driving=False
        _mileage=12.0

    def setManufacturer(self,man):
         self._manufacturer=man

    def setBrand(self,brand):
         self._brand=brand

    def setMaxSpeed(self,speed):
         self._maxSpeed=speed

    def setMileage(self,mileage):
         self._mileage=mileage

    def stop(self,m):
         self._driving=False
         self._mileage=self._mileage+m

    def start(self):
        self._driving=True

    def getManufacturer(self):
        return self._manufacturer;

    def getBrand(self):
        return self._brand

    def getMaxSpeed(self):
        return self._maxSpeed

    def getMileage(self):
        return self._mileage

    def getDrivingStatus(self):
        return self._driving

    def display(self):
        print("Manufacturer : ",self._manufacturer)
        print("Brand : ",self._brand)
        print("Max Speed : ",self._maxSpeed)
        print("Mileage : ",self._mileage)
        print("Driving Status : ",self._driving)
        
