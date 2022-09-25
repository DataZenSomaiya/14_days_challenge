#Input
name = input("What is your name? ")
print("Hello "+ name)
print(' ')

#Type Conversion
birth_yr = input("Enter your birth year ")
age = 2022 - int(birth_yr)
print(f'Your age is : {age}')
print(' ')

#Strings
course = 'Python for Beginners'
print(course)
print(course.find('r'))
print(course.replace('n','4'))
print('Python' in course)
print(' ')

#Arithmetic Operators
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
x = 10
x = x + 3
print(x)
print(' ')

#Exercise
weight = input("Weight : ")
unit = input("(K)g or (L)bs : ")
unit.upper()
if unit == "K":
    conv = float(weight)/0.45
    print(f'Weight in Pounds : {conv}')
else:
    conv = float(weight) * 0.45
    print(f'Weight in Kilogram : {conv}')

#While loop
i = 1
while i<=5:
    print(i)
    i = i+1
j = 1
while j<=10:
    print(j * '*')
    j = j+1

#Lists
names = ["John", "Bob", "Rewa", "Sam"]
print(names)
names[0] = "Jon"
print(names[0:3])

#Objects
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
numbers.insert(0,-1)
print(numbers)
numbers.remove(3)
print(numbers)
print(1 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)
