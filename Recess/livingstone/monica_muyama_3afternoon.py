#1. Create a list with 5 items (names of people) and write a python program to output the 2nd
# item.
people = ["Monica", "Joseph", "Immaculate", "Jeremiah", "Modesta"]
print(people[1])
print("********************************************************************")

#2. Write a python program to change the value of the first item to a new value
people[0] = "Justine"
print(people)
print("********************************************************************")

#3. Write a python program to add a sixth item to the list
#people[5] = "Emma"
print(people)
print("********************************************************************")

#4. Write a python program to add “Bathel” as the 3rd item in your list

#5. Write a python program to remove the 4th item from the list
people.pop(3)
print(people)
print("********************************************************************")

#6 use negative indexing to print last item in your list
print(people[-1])
print("********************************************************************")

#7. Create a new list with seven items and use a range of indexes to print the 3rd, 4th and 5th items
fruit_list =["apple", "banana", "cherry", "pineapple", "paw paw", "straw berry", "orange"]
print(fruit_list[2:5])
print("********************************************************************")

#8 write  a  list of countries and make a copy of it
countries = ["Uganda", "kenya", "Tanzania", "Rwanda"]
conutries_copy = countries.copy()
print(countries)
print(conutries_copy)
print("********************************************************************")

#9  Write a python program to loop through the list of countries
for country in countries:
    print(country)
print("********************************************************************")

#10  Write a list of animal names and sort them in both descending and ascending order.
animals = ["cat", "dog", "cow", "rabbit", "goat", "donkey"]
animals.sort()
print(animals)
animals.sort(reverse = 1)
print(animals)
print("********************************************************************")

#11  Using the list above, write a python program to output only animal names with the letter 
# ‘a’ in them
for animal in animals:
    if "a" in animal:
        print(animal)
print("********************************************************************")

#12 Write two lists, one containing your first names and the other your second names. Join 
# the two lists.
first_names = ["Monica", "Precious", "Collins", "karim", "Marvis", "Moussa"]
second_names =["Muyama", "Kyomuhendo", "Kato", "Musabe", "Bazziwe", "Kimuli"]
#full_names = [first_names + "" + second_names]
#print(full_names)

#alternatively
full_names = first_names
full_names.extend(second_names)
print(full_names)
print("********************************************************************")
print("********************************************************************")

#Exercise 2
#1. Consider the tuple below;
x = ("samsung", "iphone", "tecno", "redmi")
print("********************************************************************")

#Write a python program to output your favorite phone brand.
print(x[0])
print("********************************************************************")

#2. Use negative indexing to print the 2nd last item in your tuple.
print(x[-2])
print("********************************************************************")

#3. Using the phones list above, write a python program to update “iphone” to “itel”
m_list = list(x)
m_list[1] = "itel"
x = tuple(m_list)
print("********************************************************************")

#4. Write a python program to add “Huawei” to your tuple.
my_list = list(x)
my_list.append("Huawei")
x = tuple(my_list)
print(x)

print("********************************************************************")

#5. Write a python program to loop through the tuple above.
for i in x:
    print(i)
print("********************************************************************")

#6. Write a python program to remove/delete the first item in your tuple.
n_list = list(x)
n_list.remove(n_list[0])
x = tuple(n_list)
print("********************************************************************")

#7. Using the tuple() constructor, create a tuple of the cities in Uganda.

#8. Write a python program to unpack your tuple.
#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
#10. Write two tuples, one containing your first names and the other your second names. Join 
#the two tuples.
#11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "orane", "yellow")
colors_multiplied = colors*3
print(colors_multiplied)
print("********************************************************************")

#12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
z = 0
for number in thistuple:
    if number == 8:
        z += 1
print(z)
print("********************************************************************")

#Exercise3 (Sets)
#1. Use the set() constructor to create a set of 3 of your favorite beverages.
favourite_beverage = set(("coffee", "tea", "juice"))
print(favourite_beverage)
print("********************************************************************")

#2. Use the correct method to add 2 more items to the beverages set.
favourite_beverage = favourite_beverage.add("water")
#favourite_beverage = favourite_beverage.add("cocktail")
print(favourite_beverage)
print("********************************************************************")

#3. Given the set below;
#Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
  print("Microwave is present in the set")
else:
  print("Microwave is not present in the set")
print("********************************************************************")

#4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet)
print("********************************************************************")

#5. Write a python program to loop through the set above.
for i in mySet:
    print(i)
print("********************************************************************")

#6. Write a set of 4 items and a list of two items. Write a python program to add elements in 
#the list to elements in the set.
mset = {"axe", "panga", "knife", "fork"}
mlist = ["spoon", "laddle"]
mset = mset.update(mlist)
print(mset)
print("********************************************************************")
#7. Write two sets, one containing your ages and the other your first names. Join the two 
#sets.
ages = {18, 21, 25}
first_names = {"Monica", "Lucy", "John"}
# Join the two sets
joined_sets = ages | first_names
# Print the joined sets
print(joined_sets)
print("********************************************************************")

#Exercise4 (Strings)
#1. Declare two variables, an integer and a string and use the correct method to concatenate 
#the two variables.
age = 20
name = "My name is Monica and I am {} years old"
print(name.format(age))
print("********************************************************************")

#2. Consider the example below;
txt = " Hello, Uganda!  "  
print("********************************************************************")

#Output the string without spaces at the beginning, in the middle and at the end.
txt = txt.replace(" ", "")
print(txt)
print("********************************************************************")

#3. Write a python program to convert the value of ‘txt’ to uppercase.
print(txt.upper())
print("********************************************************************")

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt.replace("U", "V")
print(txt)
print("********************************************************************")

#5. Using the code below, write a python program to return a range of characters in the 2nd
#, 3rd and 4th position.
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)
print("********************************************************************")

#6. The piece of code below will give an error when output;
#x = “All “Data Scientists” are cool!” 
#Write a python program to correct it.
x = "All \"Data Scientists\" are cool!"
print(x)
print("======================================================")


#Exercise5 (Dictionaries)
#1. With reference to the dictionary below, write a python program to print the value of the 
#shoe size. 
#Add this dictionary to your .py file
Shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40    
} 
    
print(Shoes["size"])
print("********************************************************************")

#2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print("********************************************************************")

#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)
print("********************************************************************")

#4. Write a python program to return a list of all the keys in the dictionary above.
#shoes_list = list(Shoes.values)
print("********************************************************************")

#5. Write a python program to return a list of all the values in the dictionary above.
#print(shoes_list)
print("********************************************************************")

#6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes.keys():
    print("size exits")
else:
    print("size doesn't exist")
print("********************************************************************")
    
#7. Write a python program to loop through the dictionary above.
for i in Shoes:
    print(i)
print("********************************************************************")

#8. Write a python program to remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)
print("********************************************************************")

#9. Write a python program to empty the dictionary above.
Shoes.clear()
print("********************************************************************")

#10. Write a dictionary of your choice and make a copy of it.
dict = {1: 'python', 2: 'java', 3: 'kotlin', 4: 'C++', 5: 'PHP'}
dict_copy = dict.copy()
print(dict)
print(dict_copy)
print("********************************************************************")

#11. Write a python program to show nested dictionaries
my_team = {
    "" : {
        "name" : "Precious",
        "role" : "team leader"
    },
    "member2" : {
        "name" : "Collins",
        "role" : "system analyst"
    },
    "member3" : {
        "name" : "Karim",
        "role" : "project manager"
    },
    "member4" : {
        "name" : "Monica",
        "role" : "supervisor"
    }
}
print(my_team)