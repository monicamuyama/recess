# An exception is an event which occurs during the execution of a program that disrupts
# the normal flow of the programs instructions

# Exception Handling
# if you have code that may raise an exception, place it in the try: block,
# after try, include an except statement followed by code that
# handles the problem elegantly
# a single try block can have multiple except statements.
# This is useful when a try block contains statements that may throw different
# types of exceptions
# You can provide generic clause which handles any exception
# After the exception clause, you can include an else clause
# the code in the else block executes if the code in
# the try block does not raise an exception

# try except
# Python program to handle simple runtime error

import os
a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))

    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")

# Program to handle multiple errors with one except statement


def fun(a):
    if a < 4:

        # throws ZeroDivisionError for a = 3
        b = a/(a-3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

try:
    fh = open("test", "w")
    fh.write("This is a test")
except IOError:
    print("Error: can't open the file or read the file")
else:
    print("Written content in the file successfully")
    fh.close()


# try finally block
# No exception Exception raised in try block
try:
    k = 5//0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')

# 1SyntaxError:
# This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
# 2TypeError:
# This exception is raised when an operation or
# function is applied to an object of the wrong type, such as adding a string to an integer.
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")


# 3NameError:
# This exception is raised when a variable or function name is not found in the current scope.
# 4IndexError:
# This exception is raised when an index is out of range for a list, tuple, or other sequence types.

# 5KeyError:
# This exception is raised when a key is not found in a dictionary.
# 6ValueError:
# This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
# 7AttributeError:
# This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
# 8IOError:
# This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
# 9ZeroDivisionError:
# This exception is raised when an attempt is made to divide a number by zero.
# 10ImportError:
# This exception is raised when an import statement fails to find or load a module.

# Raising one's own exception
class CustomException(Exception):
    pass


def divide_numbers(a, b):
    if b == 0:
        raise CustomException("Cannot divide by zero")
    return a / b


try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except CustomException as e:
    print("Error:", str(e))


# File Handling in python
# Before working on a file, you need to first open the file. the open() function
# is used to open the file. It takes in two parameters: the filename and the mode

# modes for file opening
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

# a file named "monica", will be opened with the reading mode.

file = open('monica.txt', 'r')

# This will print every line one by one in the file
for each in file:
    print(each)

# read function extracts all characters in a file
print(file.read())

# You can read a certain number of characters in a file
print(file.read(10))
file.close()

# we can also split the text into lines using split function
# Python code to illustrate split() function
with open("monica.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

file.close()

# writing to a file
# Open the file in write mode before you can write to it
# use the write function

file = open("monica.txt", "w")

file.write("Hello this is Monica")
file.close()

# Python code to illustrate append() mode
file = open('monica.txt', 'a')
file.write("This will add this line")
file.close()


def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)


def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " +
              new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
