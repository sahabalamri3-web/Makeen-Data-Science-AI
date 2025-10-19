w = 20
l = 50
area = w * l
print(area)

name="sahab"
age=25

print("Hi \t"+name)
print("My name is \t"+name)
print(type(w))
print(type(name))

x= 60
x2 = 99
x3 = 90

avg = (x+x2+x3)/3
print(avg)

canValume= 20
canValume =canValume +4
print(canValume) #updating the value of canValume
"""
5name #syntaxError start with number or sign or _
_name
$name
canValume #camle case
"""
BOATLE_VOLUME = 7 #CONSTANT should be a CAPTELE LETERRS 
BOATLE_VOLUME = 4.0
textRate = 2  #variable
print(BOATLE_VOLUME)

"""
Example::
this program computes the volume in liters of six-pack of sode cans
and the total volume of six-pack and  two-liter bottle
"""
#liters in a 12-ounce can
CAN_VALUME = 0.355

#liters in two-liter bottle
BOATLE_VOLUME = 2

#number of cans per pack
cansPerPack = 6

#calculate total volume in the cans
totalVolume = cansPerPack * CAN_VALUME
print("A six-pack of 12-ounce cans contains", totalVolume,"liters")

#calculate total volume in the cans and 2 liter bottle
totalVolume = cansPerPack + BOATLE_VOLUME
print("Total volume in the cans and 2 liter bottle ",totalVolume,"liters")

x= 2 + 2 ** 4 # ** is stronger than add
print(x)
b= 2 * 2 ** 4
print(b)
a=2 + 10/2  
print(a)

firstName = "Sahab"
lastName = "Al-amri"
fullName = firstName + " " + lastName
print(fullName)


a=1
b=1
c=1
x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
print(x1)
x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(x2)

x = 5 // 2 # // number shuld be integer not float
print(x)
a=8 // 3
print(a)
a1=10 // 3
print(a1)
a=8  # if output 0 it is binary number 1 is ood number
b= a%2
print(b)


#example2

#baises =int(input("Enter your number ="))
riales=baises//1000 #الباقي من الالف
baises=baises%1000 #المتبقي من الريال 
print("riales =",riales,"\n","baises =",baises)
 
 
#baises =int(input("Enter your number ="))

if baises>1000:
    riales=baises//1000
    baises=baises%1000
    print(riales)
    print(baises)
else:
    print("Error")
    
#example3  "string"

message = 'hi "this is quote" '
print(message)

print(len(message))


        