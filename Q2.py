#first we need to import the class from the file 
from CashRegister import CashRegister 
r=CashRegister() #create an object of type CashRegister
#calling method addItem
r.addItem(1.5)
#calling getTotal and getCount method
print(" Total price ",r.getTotal(),"Total Count : ",r.getCount())
print("Change after payment of 3.5 is ",r.giveChange(3.5))
