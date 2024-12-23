import time

print("Welcome to Junior's Signature Bank")
account_balance = 1000

user_pin = "1234"


entered_pin = input("Please enter your pin: ")
if entered_pin != user_pin:
  time.sleep(1)
  print("Incorrect Pin, Please try again...")
else:
  time.sleep(1)
  print("Pin correct")
  atm_on = True
  while atm_on:
    print("Main Menu:")
    print("1. Check balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    option = input("Main Menu\nChoose an option (1,2,3,4): ")
    if option == "1":
      print(f"Your account balance is ${account_balance}")
      print("____________________")
      print("____________________")
    elif option == "2":
      deposit_amount = float(input("Enter Deposit Amount: "))
      account_balance += deposit_amount
      print(f"Successfully deposited ${deposit_amount}\nCurrent account balance is ${account_balance}")
      print("____________________")
    elif option == "3":
      withdrawal_amount = float(input("Enter Withdrawal Amount: "))
      if withdrawal_amount > account_balance:
        print("Insufficient Funds")
        print("____________________")
      else:
        account_balance -= withdrawal_amount
        print("Withdrawal Successful")
        print("____________________")
    elif option == "4":
      print("Are you sure you want to exit?")
      ans = input("yes/no")
      if ans.lower() == "yes":
        atm_on = False
        print("Goodbye...")
      elif ans.lower() == "no":
        pass
      else:
        print("Incorrect input")
        
    else:
      print("Invalid input\nPlease try again")
      print("____________________")
      