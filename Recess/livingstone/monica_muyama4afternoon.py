#Functions
#used to write code that is clear, reusable and maintainable
#def function_name():
#arguments and parameters
#arguments are always specified after the function name
#Parameters nb
def afternoon(first_name, last_name):
    print(f"Hi {first_name} {last_name} goodafternoon")
    print("many people have attended")

#calling a function
   # afternoon() # doesn't print
afternoon("monica", "muyama")

import module
print(module.product(8,4))


#input and output in python
#input('prompt')

#Example of input
name = input("Enter your name: ")
print("My name is ," + name)

#Example 2
number = int(input("Enter your age: "))
square = number*number
print(square)

#Example 3 : Multiple inputs in python have to be of the same datatypr
s,r,q = map(int, input("Enter the values: ").split())
print("the values are : ", end = "")

#How to input from a tuple
w = (2,4,5,7,8,9)
print("current tuple")
print(w)

E = list(w)
E.append(int(input("Enter new value: ")))
w = tuple(E)
print("Updated tuple")
print(w)

#How to input from a 
my_list = list(map(int, input("enter the list values: ").split()))
my_set = set(map(int, input("enter the set values: ").split()))
print(my_list)
print(my_set)
