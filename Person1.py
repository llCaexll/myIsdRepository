class Person :
    _name=""
    def __init__(self,firstName,lastName):
        self._name = lastName + "," + firstName
        
p= Person("Harry","Morgan") 
print(p._name)
