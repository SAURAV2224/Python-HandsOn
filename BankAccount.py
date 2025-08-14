class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
            return f"Account owner: {self.owner} \nAccount balance: ${self.balance}"

    def deposit(self,amount):
           self.balance +=amount
           print(f"Deposit Accepted for ${amount}")

    def withdraw(self,amount):
             if (self.balance-amount) > 0:
                   self.balance -=amount
                   print(f"Withdrawal Accepted for ${amount}")
             else:
                   print("Funds Unavailable!")
            

        

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)