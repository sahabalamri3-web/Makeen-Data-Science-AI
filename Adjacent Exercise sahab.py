
numbers = input("Enter number: ")
previous = numbers

while numbers != "":
    numbers = input("Enter number: ") #new input
    if numbers == previous and numbers != "":
        print("This number is repeated!")
    previous = numbers