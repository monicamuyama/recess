#Classes
#Example Car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

my_car = Car("Toyota", "corolla", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine
my_car.stop_engine

# Example2 Two Banking
class BankAccount: 
    def __init__(self, balance,  account, name):
        self.balance = balance
        self.account = account
        self.name = name
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        else:
            self.balance = self.balance - amount
            print(self.balance)

# Example3 Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Example4: University Student
class Student: 
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self. course = course

    def display_details(self): 
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Course: ", self.course)
# create object
my_student = Student("Monica",2000, "software engineering")

# display details
my_student.display_details()

#Object
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello, my name: ", self.name)
        print("i am ", self.age, "years old")

#create a person object
my_person1 = Person("monica", 20)
my_person2 = Person("Vicky", 14)

#Access the person object attr
print(my_person1.name)
print(my_person1.age)
print(my_person2.name)
print(my_person2.age)

#invoke the method
my_person1.greet()
my_person2.greet()

#Exercise: class circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 2* 3.14 * self.radius * self.radius
    
    def calculate_circumference(self):
        return 2* 3.14 * self.radius 
my_circle = Circle(7)
print(my_circle.radius)
print(my_circle.calculate_area())
print(my_circle.calculate_circumference())

#exercise2
#calculate and display employees bonuses(5%) of salary(employee1: 150000, employee2: 230000)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_bonus(self):
        bonus = self.salary*15/100
        return bonus
    def display_details(self):
        print(self.name, self.salary, "Bonus", self.calculate_bonus)
    
emp1 = Employee("John", 150000)
emp2 = Employee("Joan", 230000)

emp1.display_details
emp2.display_details

#Encapsulation use _
#key main goals of encapsulation
"""
1.To hide the implementation  details of an object
2. To protect objects from being changed

"""
#Example4: with a bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number # encapsulate the account number attribut
        self._balance = balance #encapsulate the balance attribute
    
    def deposit(self, amount):
        self._balance += amount 

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("insufficient balance")
    
    def get_balance(self):
        return self._balance
    
#Create a  bank object
my_account = BankAccount("2122232311", 1000)

# Access the Bank object and modify encapulated attributes indirectly
print(my_account._account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account._balance)
my_account.withdraw(100)
print(my_account._balance)

#Exercise2: Convert temperature(37 celc) from celcius to Fahrenheit
class Temperature:
    def __init__(self, celcius): 
        self._celcius = celcius
    
    def celcius_to_fahrenheit(self):
        return((self._celcius*9/5)+32)
    
my_temperature = Temperature(37)
print(my_temperature.celcius_to_fahrenheit())

#Assignment2 Show encapsulation with employee information on give a pay increment
# (Salary with employee information and new salary) e.g rom 850000 to 1000000
class Employee:
    def __init__(self, name, current_salary, new_salary):
        self._name = name
        self._current_salary = current_salary
        self._new_salary = new_salary
    
    def display_details(self):
        print(f"Name: {self._name}")
        print(f"Current Salary: {self._current_salary}")
        print(f"New salary: {self._new_salary}")
employee1 = Employee("Henry", 850000, 1000000)
employee1.display_details()