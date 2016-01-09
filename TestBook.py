from book import Book

def main():
    b=Book()
    b.setTitle("Learn Python")
    b.setAuthor("J. Ullman")
    b.setYop(2015)
    b.display()
    print("New information after changes")

    b.setYop(2013)
    b.display()
    
main()
