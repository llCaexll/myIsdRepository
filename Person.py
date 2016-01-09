class Person :
    _name=""
    def __init__(self,firstName,lastName):
        self._name = lastName + "," + firstName
    def __init__(self):
        self._name="Unknown"
	
p= Person() 
print(p._name)
