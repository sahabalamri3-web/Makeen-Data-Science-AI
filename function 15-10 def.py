length= float(input("Enter length:"))
width= float(input("Enter width:"))

def recArea(l,w):
    area=l*w
    return area
print(recArea(length,width))

###########################################################
""" function syntax:  def funName(parameters)"""
def cubeVolume(length):
    volume = length ** 3
    return volume
l = float(input("Enter length:"))
print(cubeVolume(l))#while colling the function this is arrguments

###############################################################

def fectorNum(num):#n!= n*n-1 *n-2*n-3*n-4*n*-5 .. 1
    result= 1
    for i in range(5,1,-1):
        result = result* i
    return result
n = float(input("Enter number:"))
print(fectorNum(n))
