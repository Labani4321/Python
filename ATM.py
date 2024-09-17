import time 

print("insert your ATM pin ")
password = 1234
pin = int(input("enter your ATM pin: "))

if pin == password:
    balance = 50000
    
    while True:
        print('''
    1 == Check balance
    2 == Withdraw cash
    3 == Deposit balance
    4 == Exit
    ''')

        try: 
            option = int(input("enter your option: "))
        except ValueError: 
            print("Please enter a valid option.")
            continue  

        if option == 1:
            print(f"Your current balance is {balance}")
        elif option == 2:
            withdraw_amount = int(input("Please enter the withdrawal amount: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account.")
                print(f"Your current balance is {balance}")
            else:
                print("Insufficient balance!")
        elif option == 3:
            deposit_amount = int(input("Please enter your deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print(f"Your current balance is {balance}")
        elif option == 4:
            print("Exiting the system.")
            break  
        else:
            print("Invalid option. Please try again.")
else:
    print("Wrong pin. Please try again.")
