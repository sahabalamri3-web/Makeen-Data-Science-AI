#For loop
#sever items in contener 

#name="sahab"
name=input("enter your name:")
i=0
for i in name:
    print(i)

# loop to iterate over a range of integer values

#syntax: for variable range()
for k in range(5):
    print(k)
#########################################################
    
for k in range(5):
    print("Noor")#will print noor 5 times
###########################################################    
total=0
for item in range(5):
    print("item: ",item)
    print("Noor")#will print noor 5 times
    total=total+10
    print("total: ",total)
############################################################
total=0
name="Ahmed"
# should focus on number of range same as variable or will get error index out og range
for i in range(5):
    print(i, name[i])
#############################################################
total=0
name=input("enter your name:")
l=len(name)#to iterate over a range of letters in name
for i in range(l):
    print(i, name[i])
##############################################################
    
for i in range(5,10,2):
    print(i)
################################################################
    
for i in range(1,11,+2):
    print(i)
    
################################################################
for i in range(10,1,-1):
    print(i)
#10 ....2
###########################################################
    
#Print the balance at the end of each year for a number of years

#years=5
balence=10000
rate=0.05
years=int(input("Enter number of years:"))

for i in range(1,years+1):
    balence=balence+(balence*rate)
    print(i,balence)

####################################################################
    
'''
Including end=“” as the last argument to the print function prints an empty string after the 
arguments, instead on a new line

The output of the next print function starts on the same line
'''

for i in "Ali":
    print(i, end=" ")# the next print function starts on the same line
print("I am a student", end=" ")
print(12)
print("I love coffee", end=" ")
print(" and chai")
print(12)
#######################################################################33
'''
nested for loop
'''

for i in range(1,5):
    for j in range(1,5):
        print(i**j,end="") # i=1**1 ... 2**2..3**3 
    print()
        
#######################################################################33
'''
* * * * 
* * * * 
* * * *
'''
for i in range(3):#يتكرر 3 مرات 
    for j in range(4):#داخله بيتكرر 4 مرات
        print("*", end=" ")
    print()#new line 
#######################################################################
'''
* 
* * 
* * * 
* * * *
'''
for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print()
#######################################################################
'''
   *
  **
 ***
****
'''
for i in range(4):
    for j in range(4-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
         
    print()
#######################################################################
    