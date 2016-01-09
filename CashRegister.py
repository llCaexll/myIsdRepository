class CashRegister :
# default constructor of object which going to set itemCount and     totalPrice to zero initially. 
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
#additem method take price of item as input and it add this price to total price and increase the count of item by 1.
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
#this method returns the value of totalPrice of items.
   def getTotal(self) :
      return self._totalPrice
      
 
#this method returns the count of items.    
   def getCount(self) :
      return self._itemCount

#this method set value of itemCount and totalPrice to 0
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

#method getPounds that yields the amount of the total sale as a sterling value without the pence.
   def getPounds(self):
       return self._totalPrice*0.01

#method giveChange(self, payment) that gives change for the provided payment.
   def giveChange(self,payment):
        return payment-self._totalPrice

register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register2 = CashRegister()
register2.addItem(1.90)
print("Total Items ",register1._itemCount,"Total Price ",register1._totalPrice)
print("Returned change on payment of 2 is %.2f"%register1.giveChange(2))
print("Total Price in pound is %.4f"%register1.getPounds())

