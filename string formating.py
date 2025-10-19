"""
string formatting:
using the % operator (modulo)
for
string :: 's'
int(decimal) :: 'd'
float(decimal) :: 'f'

"""
#order of values matters each % have value whatever it is s,d,f 
name = 'sahab'
age = 25
city = "salalah"
print("Hello, My name is %s and I'am %d , my city is %s" %(name, age,city))

##############################################
book = "English"
bookPrice = 10.55
discount = 5
print("The price of my %s book is %.2f and it has a discount of  %d%%" %(book,bookPrice,discount))
#############################################
num1= 1.2345
num2 = 10 # I want the output: 10%
print("num1:  %10.3f \nnum2:%10d%% "%(num1,num2))
