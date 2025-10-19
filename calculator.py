"""
num1 = int(input("Enter first number :: "))
num2 = int(input("Enter Second number :: "))

Addition = num1 + num2
print(num1 ,"+", num2, "=",Addition)

Subtraction = num1 - num2
print(num1 ,"-", num2, "=",Subtraction)

Multiplication = num1 * num2
print(num1 ,"*", num2, "=",Multiplication)

Division = num1 / num2
print(num1 ,"/", num2, "=",Division)
"""
'''
string formatting:
using the % operator (modulo)
'''
# 'd' for int,'f' for float, 's' for string
price = 1.2199967
print("the price is: %10.5f " %(price)) 
price2 = 3.989889
discount = 5
print("the price is: %10.5f  And the discount is %d" %(price2,discount)) 
number1 = 1234
number2 = 13454
s= 1244.45
print("number1 is: %10d " %(number1))
print("number2 is: %10d   " %(number2))
#####################
great="Hello"
great2="Good Morning"
print("%10s  %-5s" %(great,great2))

d=4
print(" %10d%%%%  " %(d))
#mothed is object
great2="Good Morning"
print(great2.upper())
print("Ali".upper())
print(great2.lower())
print(great2.title())#just the first letter is upper case
print(great2.swapcase())# first letters is in lower case and the others in upper
print(great2.capitalize())# just the first letter is upper case


titel = "python everyone"
#output: python program
#titel = titel.replace("everyone","program")
titel = titel.replace("everyone","Everyone")
print(titel)
'''
#find mothed
txt1 = "Hello, welcome to my world."
x = txt1.find("w",8,25) # if there is no s will return -1 find("",start,end)
print(x)

floor = int(input("enter floor number:: "))
if floor == 13:
    print("Invalid input please enter floor agin")
    
floor = int(input("enter floor number:: "))
if floor>13:
    actulfloor = floor - 1
    print(actulfloor)
else:
    print(actulfloor)
'''
"""
price = int(input("Enter price: "))

if price>200:
    Discount=price*0.05
    fPrice = price-Discount 
    print("the Discount",Discount)
    print("the price after Discount ",fPrice)

else:
   print(price)
   
   """
num1 = int(input("Enter first number :: "))
num2 = int(input("Enter Second number :: "))
operater =(input("/ * + - "))
if operater== "+" :
    print(num1 ,"+", num2, "=",operater)
elif operater== "-" :
    print(num1 ,"-", num2, "=",operater)
    
    '''
Length = int(input("Enter the Length of a rectangle: "))
Width = int(input("Enter the width of a rectangle: "))
R=Length*Width
print("The area of the rectangle is",R)
'''