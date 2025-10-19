
#Boolean

age = 20

print(age == 20) # true
print(age != 20) # false

flage = False # output else
grade = 55 
flage = 90<=grade<=95 # false 55 not grater than 90 but less than 95

if flage:
    print("flage is true")
else:
     print("flage is fales")


######################################################
age=25
if age>=20 and age <=20: #لا يتحقق الشرط false
    print("you are 20 years")
else:
    print("you are above 20 years")
 
#######################################################

t= True ==1
f = False == 0
print(t)
print(f)

########################################################
num = int(input("Enter number:"))

print(is_positive)
if is_positive:
    print("number is positive")
else:
    print("number is nagtive")

# AND / OR OPERATERS
# if the water is liqued  >=0 and <=100
#if the water is liqued <=0 or >=100

temp=int(input("Enter temp :"))

if temp>0 and temp <100:
    print("the water is liqued")
elif temp<=0  or temp >=100:
    print("the water is not liqued")
    

flage= False
print(flage == True) # نقارنه بالترو

print(not(flage)) # true

#while loop
rate = 0.05
balance = 10000
target = 20000
year = 0

while balance < target:
      year = year+1
      benfiet = balance * rate
      balance = balance + benfiet
print(year)

########################################################33
salary = 0.0
count = 0.0
total = 0

while salary >=0:
    salary = float(input("Enter your salary "))# -1 to finish
    if salary>=0:
        total = total+salary
        count = count + 1
avg = total/count
print("print average salary :",avg)
        
#################################################################

#calculater
while True:
    x = input("Type 'exit' to end or press Enter to continue: ")
    if x=="exit" or x=="Exit":
        print("Exiting calculator...")
        
        break # to stop  exit
         
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
   
    if operator == "+":
        print("the result from Addition (+)  : ", num1 + num2)
    elif operator == "-":
        print("the result from Subtraction (-):",num1 - num2)
    elif operator == "*":
        print("the result from Multiplication (*) : ", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("the result from Division (/)  : ", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
           print("Invalid operator!")

#########################################################3

name = input("Enter username: ")
password =int(input("Enter password :"))

if name == 'admin' and password == 12345:
    print("Access granted")
else:
    print(" Access denied")


#if number %3 or %5

number = int(input("Enter number1 :"))

if number % 3 == 0 or number % 5 == 0:
    print("The number is divisible by 3 or 5")
else:
    print("The number is Not divisible by 3 or 5")
    
#sum of digit number
number = int(input("Enter number1 :"))
total=0
while number>0 :
    digit=number%10
    total=total+digit
    number=number//10
print("The sum of number ",total)

#####################################33333
number = (input("Enter number :"))
counter= 0
total=0
#print(number[0])
#print(number[1])
#print(number[2])
#print(number[3])
#total = int(number[0])+int(number[1])+int(number[2])+int(number[3])
while counter < len(number):
      total = total + int(number[counter])
      counter = counter + 1
print(total)


################################################################
""" sum of digits  using while loop """

total=0.0
inputStr = input("Enter value:")
while inputStr != "":
    value=float(inputStr)
    total=total+value
    inputStr = input("Enter value:")#we write to avoid infinty loop
print("the total is:",total)


##################################################################
''' the total og nagtive number '''

inputStr = input("Enter value:")
count=0
total=0
graeterNum = inputStr[0]
while inputStr != "":
    value = int(inputStr)
    if value <0:
        count = count + 1
        total = total + value
     
    inputStr = input("Enter value:")
    if value >graeterNum:
        print("the greater number is:",value)
        
print("the total of nagtive numbers is ",count,total)

"""greater number """

inputStr = input("Enter value:")
count=0
total=0
greatest =0
while inputStr != "":
    value = int(inputStr)
    if value <0:
        count = count + 1
        total = total + value
     
    inputStr = input("Enter value:")
    
    if value > greatest :
        greatest = value
print("the greater number is:",greatest)     
print("the total of nagtive numbers is ",count,total)

''' the minmim value'''

inputStr = input("Enter value:")
count=0
total=0
minNum =0
while inputStr != "":
    value = int(inputStr)
    if value <0:
        count = count + 1
        total = total + value
     
    inputStr = input("Enter value:")
    
    if value < minNum :
        minNum = value
print("the minimum number is:",minNum)     
print("the total of nagtive numbers is ",count,total)







    

