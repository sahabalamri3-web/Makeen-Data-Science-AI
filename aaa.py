inputStr = input("Enter value:")
count=0
total=0
revalue=0
while inputStr != "":
    value = int(inputStr)
    if value <0:
        count = count + 1
        total = total + value
        revalue=value
    inputStr = input("Enter value:")
    
    if value == revalue:
        revalue = value
    inputStr = input("Enter value:")
    print("the value is repeated:",value)     
print("the total of nagtive numbers is ",count,total)