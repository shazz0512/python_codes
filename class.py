# class person:
    
#  def __init__(self,name,age):
#     self.name=name
#     self.age=age
 
#  def display(self):
#      print("my name is {} and my age is {}".format(self.name,self.age))  
     
# #we will create an object and call these functions
# person1=person('Alice', 30) 
# person1.display()
# person2=person('Bob', 35)
# person2.display()


class Bank_account:
 
 #class variable
 Bank_Branch="SBI CBD Belapur "
 
 def __init__(self,name,account_no,balance):
     self.name=name
     self.account_no=account_no
     self.balance=balance
     
 def deposit(self,amount):
     self.balance += amount
     print(f"deposit is Rs.{amount} and total balance is {self.balance}")
     
 def withdraw(self,amount):
     if amount <= self.balance:
        self.balance -= amount
        print(f"withdrawal amount is {amount} and balance is {self.balance}")
     else:
      print("Insuffient balance")
 def get_balance(self):
     return self.balance  
 def display(self):
     print(f"Name of customer {self.name} ,his account number is {self.account_no} ")     
             
account1= Bank_account('Nikhil','12345F', 1900000)
account1.display()
print(f"Name of Bank: ",account1.Bank_Branch)
account1.deposit(70000)
account1.withdraw(6000)
r_balance=account1.get_balance()
print("Current balance is",r_balance)
account2= Bank_account('Sharu','87653F', 450000)
account2.display()
account2.deposit(56430)
account2.withdraw(10000)
r_balance=account2.get_balance()
print("Current balance is",r_balance)





















       