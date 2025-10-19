name = "Ali" #you can incloude variable insed the list
traninessInAi = ["Azam", "Noor" ,"Muradi", "Muna", name]
print(traninessInAi)
contactNumber = ["9997659"]
numbers = [1,2,3,4,5]
mixList =  ["Ahmed","Muna",2,2.5]

print(mixList)
print(traninessInAi + contactNumber)
print("the length of traninessInAi lise is ",len(traninessInAi))
print(traninessInAi[1])

# print all element in list traninessInAi
 
for i in traninessInAi:
    print(i)
#########################################
    
for i in range(5):
    print(i,traninessInAi[i])
##############################################
n = len(traninessInAi) 
for i in range(n):
    print(i,traninessInAi[i])
##############################################
numbers = [2,4,-2,20,4]
maxL = numbers[0]
for i in numbers:
    if maxL<i:
        maxL=i
print("the max number in list ",maxL)   

minL = numbers[0]
for i in numbers:
    if minL>i:
        minL=i
print("the min number in list ",minL)

##############################################
'''
How to get ood or even numbers from list 
'''
numbers = [3,2,5,6]
for i in range(len(numbers)):
    if numbers[i]%2==0:
       print(numbers[i],"the number even ")
    else:
       print(numbers[i],"the number odd ")

##############################################
       
numbers = []
newNo = 0
while True:
    newNo = input("You must enter a number or q to stop: " )
    newNo.isdigit()
    if newNo == "q":
        break
    numbers.append((newNo))
print("this list of numbers is: ",numbers)


if string[newNo].isdigit():
    
else:
    