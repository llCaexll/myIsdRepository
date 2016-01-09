class Book:

     def __init__(self):
         _title=""
         _author=""
         _yop=2016

     def setTitle(self,title):
         self._title=title

     def setAuthor(self,author):
         self._author=author

     def setYop(self,year):
         self._yop=year

     def getTitle(self):
         return self._title

     def getAuthor(self):
         return self._author

     def getYop(self):
         return self._yop

     def display(self):
         print("Book  Title : ",self._title)
         print("Author : ",self._author)
         print("Year of Publication : ",self._yop)
     
