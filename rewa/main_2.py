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
