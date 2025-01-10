class BankAccount:
  def __init__(self,account_number,account_holder,balance=0):
    self.account_number = account_number
    self.account_holder= account_holder
    self.balance=balance
    
    
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      return f"Deposited {amount}\nNew balance is {self.balance}"
    return "Invalid deposit amount"
      
  def withdraw(self,amount):
    if amount > 0:
      if amount <= self.balance:
        self.balance -= amount
        return f"withdraw successful\nCurrent balance: {self.balance}"
      return "Insufficient Funds"
    return "Invalid withdrawal amount"  
    
  def get_balance(self):
    return f"Your balance is {self.balance}"
  
    
    
my_bankapp = BankAccount("1234", "john").deposit(1000)
print(my_bankapp)
print(my_bankapp.get_balance())

my_bankapp2 = my_bankapp = BankAccount("1234", "john").withdraw(0)
print(my_bankapp2)
print(my_bankapp2.get_balance())