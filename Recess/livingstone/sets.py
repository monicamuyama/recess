#store multiple items in a single variable
#unordered, do not allow duplicates
#unchangeable 
#Once a set is created, you cannot change its items, but you can remove items and add new items
setone = {"rice", "matooke", "irish"}
print(setone)

#sets can also be created using the set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#duplicates are ignored
setone = {"rice", "matooke", "irish", "irish"}
print(setone)

#length of a set
print(len(setone))

#data type
# a set can contain different datatypes
print(type(setone))

#accessing items in a set
#items in a set cannot be accessed using an index or key 
#we can use the for loop to access items
for x in setone:
    print(x)

#add items
# use add() method
print(setone.add("yam"))

#remove items
#use remove() or discard() function
print(setone.remove("irish"))

#add two sets together
#You can use the union() method that returns a new set containing all items from both sets, 
# or the update() method that inserts all the items from one set into another:
settwo = setone.union(thisset)
print(settwo)

setone.update(thisset)
print(setone)

