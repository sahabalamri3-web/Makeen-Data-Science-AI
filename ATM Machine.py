# Simple ATM Machine Simulation

# Step 1: Set correct PIN and initial balance
correct_pin = "1234"
balance = 100.0
attempts = 0
max_attempts = 3

# Step 2: Allow up to 3 attempts for PIN entry
while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Welcome!")
        break
    else:
        attempts = attempts+ 1
        if attempts < max_attempts:
            print("Incorrect PIN. Try again.")
        else:
            print("Account locked. Try again later.")
            exit()  # stop the program if PIN is wrong 3 times

# Step 3: Display menu until user chooses Exit
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is", balance, "OMR")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance =balance+amount
        print("Deposit successful! New balance is", balance, "OMR")

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance -amount
            print("Withdrawal successful! New balance is", balance, "OMR")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1–4.")
