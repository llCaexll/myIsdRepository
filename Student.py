class Student:
    
    def __init__(self):
        _firstName=""
        _lastName=""
        _number=0
        _course=""

    def setFirstName(self,firstName):
        self._firstName=firstName

    def setLastName(self,lastName):
        self._lastName=lastName

    def setNumber(self,num):
        self._number=num

    def setCourse(self,course):
        self._course=course

    def getCourse(self):
        return self._course

    def getNumber(self):
        return self._number

    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def display(self):
        print("Name of student : ",self._firstName," ",self._lastName)
        print("Student Number : ",self._number)
        print("Course : ",self._course)
        
