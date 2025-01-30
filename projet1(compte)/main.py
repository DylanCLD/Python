from fonction import Employee, Factory
from database import save_employees_to_db
import os

def main():
    print("Current Working Directory:", os.getcwd())
    
    factory = Factory("Free")

    factory.add_employee(Employee("Paul", "Schmitt", 2000))
    factory.add_employee(Employee("Elsa", "Durant", 3000, is_commercial=True))
    factory.add_employee(Employee("Pat", "Oliver", 6000))
    factory.add_employee(Employee("John", "Wayne", 5000, is_commercial=True))
    factory.add_employee(Employee("Eric", "Duval", 4000))

    factory.display_info()

    factory.save_employees_to_file()

    save_employees_to_db(factory)

if __name__ == "__main__":
    main()
