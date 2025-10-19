#Problem 1: 
name = "sahab"
age = 25
height = 1.68
print("Hello, my name is",name,"I am  ",str(age)," years old and my height is ",str(height)," meters.") 
#Problem 2: 
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


print("Addition =",number1 ,"+", number2, "=",number1 + number2)
print("Subtraction =",number1 ,"-", number2, "=",number1 - number2)
print("Multiplication =",number1 ,"*", number2, "=",number1 * number2)
print("Division =",number1 ,"/", number2, "=",number1 / number2)

#Problem 3: 

a = 15
b = 1.23
c = "sahab"

print(type(a))
print(type(b))
print(type(c))

#Problem 4:

Length = int(input("Enter the Length of a rectangle: "))
Width = int(input("Enter the width of a rectangle: "))
R=Length*Width
print("The area of the rectangle is",R)

#Problem 5:

p = int(input("Enter Principal amount:"))
r = int(input("Enter Rate of Interest:"))
t = int(input("Enter Time (in years):"))

simpleInterest = (p * r * t) / 100
print("The Simple Interest",simpleInterest)




