#Dictionaries
#used to store mutiple variables in a single variable
#have key pair values
#can have data of different data types

mydict = {
    "phone": "iphone",
    "iphonemodel": "iphone14",
    "year": 2023,
    "colors": ["blue", "black", "red"]

}

#length
print(len(mydict))

#Data type
print(type(mydict))
#Data type for a specific item
print(type(mydict["phone"]))

#Accessing dictionary items
print(mydict("year"))

print(mydict.get("iphonemodel"))

print(mydict.keys())

#adding items in a dictionary
#Exercise one: use the values method to return the list of all values in a dictionary

print("Exercise One")
dict = {1: 'python', 2: 'java', 3: 'kotlin', 4: 'C++', 5: 'PHP'}
print(dict.values())

#Exercise Two: check if a key exists in your dictionary
print("Exercise Two")
dict2 = {1: 'python', 2: 'java', 3: 'kotlin', 4: 'C++', 5: 'PHP'}
key = 4
if key in dict2:
    print("Key exists in dict2")
else:
    print("key {key} doesnot exist in dict2")

#Exercise Three: Give an example on how to change dictionary items, how to update

print("Exercise Three ")
dict[4] = 'C#'
print(dict)
#update 
dict0 = {1: 'python', 2: 'java', 3: 'kotlin', 4: 'C++', 5: 'PHP'}
dict1 = {1: "python", 3: "javascript"}
dict0.update(dict1)
print(dict0)

#Exercise Four: how to add dictionary items
print("Exercise Four")
dict[6] = 'javascript'
print(dict)

#how to remove dictionary items
#use del function. item can be deleted using key only
del dict[3]
print(dict)

dict.clear() # remove aa entries
del dict #delete entire dictionary

#exercise Five: how to loop through a dictionary and how to nest dictionaries
print("Exercise Five ")

dict3 = {1: 'python', 2: 'java', 3: 'kotlin', 4: 'C++', 5: 'PHP'}
for x in dict3.keys():
    print(dict3[x])

#Nested dictionary
my_team = {
    "member1" : {
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

print(my_team["member2"]["name"])

#Exercise: use condition to show how to use booleans 
print("Exercise with boolean")
is_female = True
if is_female:
    print("You are female")
else:
    print("You are male")

