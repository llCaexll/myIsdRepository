from student import Student
def main():
    s=Student()
    #initialization of all values
    s.setFirstName("Harry")
    s.setLastName("Morgan")
    s.setNumber(1134)
    s.setCourse("Computer")
    s.display()

    #changes are performed here
    s.setFirstName("Henry")
    s.setCourse("Computer Engineering")

    print("Student information after change : ")
    s.display()

    

main()
