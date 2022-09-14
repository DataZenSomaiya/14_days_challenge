print("Python Exercises\n")
Name = ("John Smith")
Age=20
Status = ("New patient")
print ("Name:"+str(Name),"\t Age:"+str(Age),"\t Status:"+str(Status))
print(end="\n")

#calculator
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
sum=a+b
print(sum)
print(end="\n")

#weight convertor
weight=int(input("Enter your weight:"))
unit=input("(K)g or (L)bs:")
if unit.upper()=="K":
    converted=weight/0.45
    print("Weight in Lbs:" + str(converted))
else:
    converted=weight*0.45
    print("Weight in Kgs:"+ str(converted))

print(end="\n")

#list
numbers=[1,2,3,4,5,6,7,8,9,10]
for item in numbers:
    print(item)
i=0
while i< len(numbers):
    print(numbers[i])
    i=i+1

print(end="\n")

#range function
numbers=range(5,10,2)
for number in range(5):
    print("Number is:"+str(number))
    print(end="\n")

#tuple
a= ("apple", "banana", "cherry")
print("Tuples are:"+str(a))


