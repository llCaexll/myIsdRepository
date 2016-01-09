from Car import Car
def main():
    c=Car()
    c.setManufacturer("Ferrari")
    c.setBrand("F1")
    c.setMileage(12)
    c.start()
    c.display()
    print("\nStoping Car\n")
    c.stop(0.5)
    c.display()

    print("\nStarting Car Again\n")
    c.start()
    c.display()
    
main()
