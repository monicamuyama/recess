#control flow

"""
if condition1:
print(True)
elif:
print(False)
else:
print("hello there")
"""
age =20
if (age<18):
    print("you are under age")
elif (age >= 18 and age < 65):
    print("you are an adult")
else:
    print("you are a senior citizen")   

#loops
# 2 loops (for, while)
Fruits = ["Mango", "Pear", "Strawberry", "Paw paw", "Cherry"]
for i in Fruits:
    print(i)   

#while loop
x = 0
while x < 5:
    print(x)
    x += 1

#Break and continue statements
#Break terminates a loop
for number in range(1,10):
    if number == 5:
        break
    print(number)

#Continue statement
for number in range(1,10):
    if number == 5:
        continue
    print(number) #jumps 5

for k in Fruits:
    if k == "Strawberry":
        continue
    print(k)

#exception hndling(try except finally)
"""
try block:

except:

finally
"""
try:
    x = 10/0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("this is always executed")

 # Example with dictionary

emotions = {'happy': 'I am glad to hear you are happy',
'sad': 'sorry, is there a way i can be of help',
'angry' : "So sorry, don't in a haste to make a decision and try to stay calm",
'fearful' : "i know that fear can be challenging, but you gat all it take",
'disgusted' : "It's unfortunate that you are disgusted"}   

#prompt user to enter emotions
user_emotion = input("How are you feeling today")
#convert the user emotion in lower case
user_emotion = user_emotion.lower()
if user_emotion in emotions:
    print(emotions[user_emotion])

else:
    print("okay")

#Exercise 1 
#write program to ask students about there mental health
#Prompt students on a scale of 1 to 10 to rate their mental health
student_mental_health_status = {
1: "I"
}

name = input("What's your name")

rating = input("Hello " + name + "can you rate your mental health on the scale of 1 to 10")

if rating in range(1-10):
    output = "Hello " + name + " your mental health rating is {rating}  /10"
else:
    print("you didnot enter the rignht option, values range from 1 to 10")







