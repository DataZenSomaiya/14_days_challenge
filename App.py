print('Hello World')
age = 20
age = 30
print(age)
first_name = "Hardik"
is_online = False
name = input("what is your name? ")
print("Hello " + name)
# Type of Conversion
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)
print(age)
# Test
first_number = input("number ")
second_number = input("number ")
Sum = int(first_number) +  int(second_number)
print(Sum)
# Strings
course = "Investment model"
print(course.find('s'))
print(course.replace('model', 'function'))
#Arithmetic operation
print(10**3)
#Logical operators
price = 25
print(price>10 and price<30)
# If Statements
temperature = 35
if temperature > 30:
    print("It's a hot Day")
    print("Drink plenty of water")
elif temperature > 20:
    print("it's a nice day")
# Exercise
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
