#used to store items in a single variable
#ordered, changeable, allow duplicates
Fruits = ["Mango", "Pear", "Strawberry", "Paw paw", "Cherry"]
#length
print(len(Fruits))
#type
print(type(Fruits))
#Items in lists can be accessed using indicies, negative and positve
print(Fruits[3])
print(Fruits[-1])
#Items an be accessed in a range, last range is excluded
print(Fruits[1:4])
print(Fruits[:4])
print(Fruits[1:])
#Adding list items
#Append adds item at the end
Fruits.append("Guava")
#Insert
Fruits.insert(1, "Berry")
#Removing items
Fruits.remove("Pear")
#remove using an index, use pop
Fruits.pop(2)
