# Question 1 – Variables and Input
name=input(" Enter your name:")
age=int(input("Enter your age: "))

print("Hello %s you are %d years old" %(name,age)) 

#Question 2 – Data Types and Arithmetic Operators

number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
add=number1+number2
print("The sum is: " ,add)

# Question 3 – Arithmetic and Relational Operators
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
numbers=number1>number2
print(numbers)
print("Is the first number greater? ",numbers)

#using if else
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
if number1>number2:
    print("the first number greater")
else:
    print("the second number is smaller")
#Question 4 – Boolean Operators
age=int(input("What's your age: "))
nationality=input("What's your nationality: ")
if age >= 18 and nationality == "oman":
    print(" you are eligible to vote in Oman")
else:
    print(" you are Not eligible to vote in Oman")

#Question 5 – If Statement 
num = int(input("Enter number:"))
positive=num>0
print(positive)
if positive:
    print("number is positive")
else:
    print("number is nagtive")
    

# Question 6 – If / Else'
num = int(input("Enter number:"))
if num %2==0:
    print("number is even")
else:
    print("number is odd")

# Question 7 – If / Elif / Else
mark = int(input("Enter your mark:"))

if mark>=90:
    print("Excellent")
elif 70<= mark <90:
    print("Good")
elif 50<= mark <70:
    print("Pass")
else:
    print("Fail")

#Question 8 – Nested If

age=int(input("Enter your age: "))
licenses=input(" Do you have a driving license?  ")

if age>=18 and licenses=="yes":
    print("You can drive.")
elif age>=18 and licenses=="no":
    print("You need a license to drive.") 
    
else:
    print("You are too young to drive.")

# Question 9 – While Loop
num=1
while num <=5:
      print(num)
      num=num+1
# Question 10 – While Loop with If Condition

num = int(input("Enter number:"))
count=0
while count<=num:
     if count%2==0:
        print(count) 
        #print(" The number is even.",count)
     count=count+1
    
    





