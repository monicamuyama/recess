#Used to store items in a single variable
#they are ordered, unchangeble and allow duplicates

phones = ("samsung", "tecno", "iphone", "samsung")
print(phones)
print(len(phones))
tuple1 = ("mary", "martha", "Monica", "Mercy")
tuple2 = (500,400,300,200,100)
#Accessing items in a tuple
#accessed using indicies
print(phones[2])
#inorder to modify a tuple, first conver it into a list, modify then convert back
tuple1 = ("mary", "martha", "Monica", "Mercy")
z = list(tuple1)
z.append("Marion")
tuple1 = tuple(z)

#adding two tuples
laptops = ("Dell", "HP", "Ace")
laptop =("lenovo",)
laptops  += laptop
print(laptops)

newStock = laptops + laptop
print(newStock)

#for loops
for m in tuple1:
    print(m)
