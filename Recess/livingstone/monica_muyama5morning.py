#Inheritence

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...Woof")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing...")

#create Animal objects
animal = Animal("Generic animal")
dog = Dog("Spot")
cat = Cat("Flutty")

#invoke call eat method
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()

#Example 2 
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def display_info(self):
        print("Brand: ", self.brand)
        print("Color: ", self.color)

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self,brand, color, num_wheels):
        super(Car, self).__init__(brand, color)
        self.num_wheels = num_wheels 

    def display_info(self):
        super().display_info() 
        print("Number of wheels", self.num_wheels)  

    def honk(self):
        print("Honking the horn")

#create a car object
my_car = Car("toyota", "red", 4)

#Access and modify car attributes
print("Brand: ", my_car.brand)
my_car.color = "Gray"

#Invoke car methods
my_car.display_info()
my_car.move()
my_car.honk()

#Demonstrate using inheritance of to calculate area and perimeter of circle and rectangle
#Respectvely(use base class as shape)

class Shape:
    def __init__(self, length):
        self.length = length
    
class rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length) 
        self.width = width

    def area(self):
        return self.width * self.length
    
#Exampl3
#Multiple inheritance
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")
    
    
class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")

class Bird(Animal, Flyable):
    def __init__(self,name,species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        print(f"Species:", self.species)
        print(f"Name:", self.name)

#create bird object
my_bird = Bird("Pigeon", "Bird")

#Invoke the Bird object
my_bird.eat()
my_bird.fly()
my_bird.display_info()
    

#Method overriding
class Animal:
    def make_sound(self):
        print("Animal is making a sound")
    
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")

class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")

def make_animal_sound(animal):
    animal.make_sound()


#Create objects
animal = Animal()
dog = Dog()
cat = Cat()

#calling make_animal_sound fuction
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

cat.make_sound()
dog.make_sound()
animal.make_sound()

#Polymorphism. 
#allow you to write code that can work with different objects

#Method overriding occurs when a derived class provides it's 
# own definition/implementation of a method that is already defined in the base class

#method overloading allows a class to have multiple methods with the 
# same name but different parameters

#Example
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2
    
    def calculate_circumference(self):
        return 2* 3.14* self.radius
    
#create shape objects
rectangle = Rectangle(5,5)
circle = Circle(7)

#Display area
print("Rectange Area", rectangle.calculate_area())
print("circle area", circle.calculate_area())

#overloading functions
class Calculator:
    def add(self, x,y):
        return x+y
    
    def add(self, x, y, z):
        return x+y+z
#create object
calculator = Calculator()
 
#display output
#print(calculator.add(1,2))
print(calculator.add(1,2,5))

#AbstractionAllow you to focus on essential features and hide them from unnecessary details

#Example: demonstration of abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("starting the car")
    
    def stop(self):
        print("stopping the car")

class Truck(Vehicle):
    def start(self):
        print("starting the truck")
    
    def stop(self):
        print("stopping the truck")

car = Car()
truck = Truck()

car.start()
car.stop()
truck.stop()
truck.start()

# Exercise2 Demonstrate abstraction using calculating area of a circle and rectangle

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width
        
circle = Circle(55)
rectangle = Rectangle(5,7)

print("Rectange Area", rectangle.calculate_area())
print("circle area", circle.calculate_area())

#Create a receipt printing program with GUI interface, 
# a more advanced detail earns you more points
    

