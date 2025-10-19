#example3  "string"

message = 'hi "this is quote" '
print(message)

messageLen=(len(message))
print("the messege length is ",messageLen)

name = "sahab"
print(len(name))

print("-"*4)
str1 = "my name is sahab  "
str2 = "I'am 25 years old"
print(str1 + str2) #concatenation +

age=25
contactNo = "12345"



contactNo = int(contactNo)
print(type(contactNo))
print(type(contactNo), "20", age) #arguments

help(float)

s=20
a="school"
f=9.0
print("type of s ",type(s) ,"\n","type of a ", type(a) ,"\n","type of f ",type(f))
a="school" # index zero of school
print(a[0])
name1 = "Noor"
print(name1[3],name1[1],name1[2])

n = len(name1)
print(name1[n-1])

print(name1[n-2])

num = int(123)
#print(num[2]) # ERROR there is NO index for numbers

st1 = "py"
st1 = st1 + "thon" #arrgument + the output : python
print(st1)

string = "ho"
age = 20
string = string + "me"
print(string)
#print(string + "hi" + age) # Error
print(string + "hi" + str(age)) #change the age type to string so the output will be homehi20 in one word

print("hi \n word")# \n new line
"""
#length = input("Enter length of the rectangel: ")
print("the length of rectangel :")
"""
#####
"""
w=int(input("Enter the width of a rectangel: "))
l=int(input("Enter the lenth of a rectangel: "))
R=w*l
print(R)
"""
###
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
sum(num1 , num2)
             
           