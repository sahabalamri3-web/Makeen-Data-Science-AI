# compound statements / indentation 

price = float(input("Enter the price "))

if price >200:
    discount = price * 0.05
    #print("The discount price is : ", discount)
else:
    print("No Discount")
    if price <= 10:
        print("Take it free")
    else:
        print("No Discount")
print("End") # at all time will print becouse its out of  compound statements
'''
discount = ("You don't have discount")
price = float(input("Enter the price "))

if price >200:
    discount = price * 0.05
    discount=("You have discount",discount)
    
print(discount)
'''
"""
floor = float(input("Enter the floar number: "))

if floor >13:
     actualFloor=floor -1
     print("The actualFloor is ",actualFloor)
elif floor == 13:
    print("invalid input")
else:
    actualFloor = floor
    print("The actualFloor is ",actualFloor)
"""
######################
age = 20
comper = 30
if age >= comper:
    print("You are senior")
else:
    print("You are still young")
#######################################################
"""
name = "Ali" #we can write .upper()
username = input("Enter your name ").upper()
name = name.lower()
#username = username.lower()
if name == username:
    print("You can access")
else:
    print("You can't access")
  """
#######################################################
myAge = 20
youAge = 30

if myAge > youAge:
    print("I am older")
else:
    print("you are older")
#######################################################33
from math import sqrt
x = sqrt(2)
y= 2.0
diff= x*x - y
error_rate = 0.0005

if diff < error_rate:
    print("sqrt2 x sqrt2 equal 2 please procceded project")
else:
    print("you have error you cannot do this project")
    
##############################################################################   
#tem converstion
    
c = float(input("Enter temperature in celeius "))
f = c * (9/5)+32
print("the temp in fahrenheit ",f)
c1 = (f - 32) * (5/9)
print("the temp in celsius ",c1)
diff= c-c1  
print("the diffrence (c-c1)",diff)
error_rate = 0.000001
if diff < error_rate:
    print("the converstion is fine")

if c == c1:
    print("convertion is perfect!")
else:
    print("convertion is not exact , it is",c1)
########################################################################
    
x=int(input("enter number: "))


if x >= 0:
    print("the number is postive")
    if x % 3 == 0:
       print("the number is postive and divisble by 3")
    else:
       print("the number is postive but not divisble by 3")
else:
    print("the number is nagtive")
    #also if the number nagtive and divisble by 3
    if x % 3 == 0:
       print("the number is nagtive and divisble by 3")
    else:
       print("the number is nagtive but not divisble by 3")
#############################################################################
"""
odd or even number positev or nagitive numbers
"""
x=int(input("enter number: "))
if x >= 0:
      print("the number is postive")
      if x % 2==0:
         print("number is even")
      else:
         print("number is odd")

else:
    print("the number is nagtive")   
    if x % 2==0:
         print("number is even")
    else:
         print("number is odd")
####################################################################
         
value = float(input("Enter the value: "))

if value >=8:
     print("Most structures fall ")
elif value >=7:
    print("Many building destroyed")
elif value >=6:
    print("Many building considerably damaged,some collapse")
elif value >=4.5:
    print("Damage to poorly constructed buildings ")

else:
    print("NO Des")
    

########################################################################
age = int(input("Enter your age :"))

if age == 25:
    print("Free")
elif age>20:
    print("you have 30% discount")
elif age==20:
    print("you have 10% discount")
else:
    print("you don't have discount")
    
    '''
import time

time1 = float(input("Enter the time one: "))
time2 = float(input("Enter the time two: "))
if time1>time2:
     print("time one comes first ")
elif time1>time2:
     print("time one comes first ")
    
elif value >=6:
    print("Many building considerably damaged,some collapse")
elif value >=4.5:
    print("Damage to poorly constructed buildings ")

else:
    print("invalid")
    
    
    
    '''

from time import time

time1 = input("Enter the first time: ")
time2 = input("Enter the second time: ")
if time1>time2:
     print("time one comes first ")
elif time1==time2:
     print("time one same as time two ")
else:
    print("time two comes before time one")
    
####################################################33
from datetime import datetime

time1 = input("Enter the first time: ")
time2 = input("Enter the second time: ")
#tranform str to real time
trans = "%H:%M"
t1 = datetime.strptime(time1,trans).time()
t2 = datetime.strptime(time2,trans).time()

if t1>t2:
     print(t2," comes first ",t1)
     
elif t1<t2:
    print(t1," comes before ",t2)
     
else:
    print(t1," same as ",t2)
    
####################################################
import time

time1 = input("Enter the first time: ")
time2 = input("Enter the second time: ")
#tranform str to real time
trans = "%H:%M"
t1 = time.strptime(time1,trans)
t2 = time.strptime(time2,trans)

if t1>t2:
     print(" time 1 comes first ")
     
elif t1<t2:
    print("time2 comes before time1 ")
     
else:
    print(" time 1 same as time 2 ")

######################################################33333
    
    import time
time1 = input("Enter the first time: ")
time2 = input("Enter the second time: ")


h1 = input("Enter the first time: ")
m1 = input("Enter the time1 minuetes: ")
h2 = input("Enter the second time: ")
m2 = input("Enter the time2 minuetes: ")

h1,m1,= time.strptime(h1, "%H:%M")
if h1>h2:
     print(" time 1 comes first ")
     
elif h1>h2:
    print("time2 comes before time1 ")
     
else:
    print(" time 1 same as time 2 ")
    if m1>m2:
         print(" time 2 comes first ")
    elif m2>m1:
         print(" time 1 comes first ")
    else:
        print(" time 1 same as time 2 ")
    

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
is_positive = num >=0
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






    

