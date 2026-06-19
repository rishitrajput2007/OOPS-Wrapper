class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    # Getters
    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    # Setters
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


person = None
employee = None
manager = None

print("--- Python OOP Project: Employee Management System ---")

while True:
    print("\nChoose an operation:")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print(f"Person created with name: {name}, age: {age}")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)

        print(
            f"Employee created with name: {name}, age: {age}, "
            f"employee ID: {emp_id}, salary: {salary}"
        )

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)

        print(
            f"Manager created with name: {name}, age: {age}, "
            f"employee ID: {emp_id}, salary: {salary}, "
            f"department: {department}"
        )

    elif choice == 4:
        print("\nShow Details")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        sub_choice = int(input("Enter your choice: "))

        if sub_choice == 1:
            if person:
                person.display()
            else:
                print("No Person Record Found!")

        elif sub_choice == 2:
            if employee:
                employee.display()
            else:
                print("No Employee Record Found!")

        elif sub_choice == 3:
            if manager:
                manager.display()
            else:
                print("No Manager Record Found!")

        else:
            print("Invalid Choice!")

    elif choice == 5:
        print("Exiting the system. All resources have been freed.\n")
        print("Goodbye !")
        break

    else:
        print("Invalid Choice!")