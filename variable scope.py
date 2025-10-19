
def main():
    #sideLength =2 error
    result = cubeVolume(2) #cubeVolume(2) or 
    return result

def cubeVolume(sideLength):#write prameter 
    return sideLength * sideLength *sideLength

print(main())

############################################################################

def main():
    sideLength =2 
    result = cubeVolume() 
    return result

def cubeVolume():
    sideLength =6
    return sideLength * sideLength *sideLength

print(main())
############################################################################

def main(l):
    result = cubeVolume(l) 
    return result

def cubeVolume(sideLength):
    return sideLength * sideLength *sideLength

length = float(input("Enter the side length: "))
print(main(length))

'''
اول شي يدخل ابيوزر اللينث بعدين ندخل الmain  و ثم نسوي كول cubeVolumeل و الرقم للي دخل نضربع ببعض 3 مرات
'''

############################################################################
balance = 10000    # A global variable
def withdraw(amount) :
    # This function intends to access the 
    # global ‘balance’ variable and deduct the amount
    global balance 
    if balance >= amount :
        balance = balance - amount

withdraw(350)
print('balance after withdraw = ', balance)

def deposit(amount):
    global balance
    balance += amount # balance = balance + amount
def check():
    global balance
    return balance
deposit(500)
withdraw(200)
print(check())
print('balance after deposit and withdraw = ', balance)