import time 
print("insert your ATM pin ")
password = 1234
pin = int (input("enter your ATM pin :"))


if pin==password:
    balance = 50000
    
    while True :
        print('''
    1 == balance
    2 == withdraw cash
    3 == deposite balance
    4 == exit
    
    ''')

    try: 
        option =int (input("enter your option:" ))
    except ValueError: 
        print(f"Please enter your valid option :")
    
    if option==1 :
        print (f"your current balance is {balance}")
    if option ==2:
        withdraw_amount = int(input("please enter the withdraw_amount: "))
        balance =balance-withdraw_amount
        print (f"{withdraw_amount} is debited from your account")
        print (f"your current balance is {balance}")

    if option ==3:
        deposit_amount = int(input("please enter your amount"))
        balance= balance+deposit_amount
        print(f"{deposit_amount} is credited to your account")
        print(f"your current balance is {balance}")
    if option ==4:
          print("existing the system")
          
    else:
        print("wrong pin please try again")
else :
    print("wrong pin.please try again")


