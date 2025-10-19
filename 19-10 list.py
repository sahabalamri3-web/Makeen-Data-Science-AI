#How to sort using sort ??????
'''
numbers = [1,16,9,4]
val = numbers[0]  
for i in numbers:
    if i < val:   
        val = i
        i+=1
print("to sort list :", val)
'''
values = [1,16,9,4]
values.sort()#[1, 4, 9, 16]
print(values)

#reverse arrgument

values = [1,16,9,4]
values.sort(reverse = True)#[16, 9, 4, 1] (reverse = False) == [1, 4, 9, 16]
print(values)
'''
age = 20
age2 = age
age = 30
print(age2) # 20
'''

mylist = [1,2,3,4]
newlist = mylist
mylist.append(5)
print(newlist)# [1, 2, 3, 4, 5]
##############################################################################################333
#To make a copy of a list

lis = [1,2,3,4]
newlist = list(lis) #copy lis into newlist
lis.append(5) #print(lis) == [1, 2, 3, 4, 5]
newlist.append(6)#[1, 2, 3, 4, 6]
print(newlist)

##################################################################################################

lis = [18, 21, 24, 33, 39, 40, 39, 36, 30, 22, 18]
#     [18, 21, 24, 33, 39, 40, 39, 36, 30, 22, 18]
#index  0 , 1 , 2 ,3 , 4  , 5 , 6, 7, 8 ,9 ,10 ,11
newlist = lis[2:5] #[24, 33, 39]
print(newlist)
nlist = lis[5:] # [40, 39, 36, 30, 22, 18]
print(nlist)

##################################################################################################

lis = []
while True:
    inputStr = input("You must enter a number or q to stop\exit: ")
    if inputStr == "q":
        break
    if inputStr.isdigit():
        lis.append(int(inputStr))
    elif inputStr[0] == '-' and  inputStr[1:].isdigit(): #negitve number and negitve value '-40k'
          lis.append(int(inputStr[1:])*-1)
    
    else:
        lis.append(inputStr)
print("The list of numbers is :", lis) #The list of numbers is : [-22, 31, '-40k', 1]

#####################################################################################################3
"""
Question 1: Collect Positive and Negative Numbers

Ask the user to enter integers (positive or negative) until they type "q".
Store positive numbers in one list and negative numbers in another.
Then print both lists.

Example:
Enter number or q to stop: 5  
Enter number or q to stop: -3  
Enter number or q to stop: 0  
Enter number or q to stop: -8  
Enter number or q to stop: q  
Positive: [5, 0]  
Negative: [-3, -8]
"""
lis = []
positiveL = []
negativeL = []
while True:
    inputInt = input("Enter number to stop/exit: ")
    if inputInt == "q":
        break
    else:
        inputInt = int(inputInt)   
        if inputInt>0:
            positiveL.append(inputInt)
        
        else:
        
            negativeL.append(inputInt)
  
print("negative numbers",negativeL)
print("positive numbers",positiveL)

#using isdigit()
negativeL = []
positiveL = [] 
while True:
    inputInt = input("Enter number or done: ")
    if str(inputInt) == "done":
        break
    if inputInt.isdigit():
        inputInt = int(inputInt)
        positiveL.append(inputInt)
    
    elif inputInt[0] == "-":
        inputInt = int(inputInt[1:])*-1
        negativeL.append(inputInt)
  
print("negative numbers",negativeL)
print("positive numbers",positiveL)

------------------------------------------------------------------------
'''
Question 2: Sum of Numbers

Keep asking the user to enter numbers until "done" is typed.
Ignore any non-numeric input.
At the end, print the sum of all valid numbers entered.

Example:
Enter number or done: 4  
Enter number or done: hello  
Enter number or done: 6  
Enter number or done: 2  
Enter number or done: done  
Sum = 12
'''
# not nagitive
mylist = []

while True:
    num = input("Enter number or done: ")
    if str(num) == "done":
        break
    if num.isdigit():
            num = int(num)
            mylist.append(num)
    elif 
print("The sum of digits is:",  sum(mylist))
##################################################################333
mylist = []
#total = 0
while True:
    num = input("Enter number or done: ")
    if str(num) == "done":
        break

    
    else:
         mylist.append(int(num))
         #total += num
print("The sum of digits is:",mylist)         
print("The sum of digits is:",  sum(mylist) )

###############################################################################33
lis = []

while True:
    inputStr = input("Enter Number: ")
    if inputStr == "done":
        break
    elif inputStr.lstrip("-").isdigit():
        lis.append(int(inputStr))
print("my list is:", lis)
print("Sum:", sum(lis))

###################################################################################3