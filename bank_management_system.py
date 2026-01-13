class Bankaccount:
    def __init__(self,name,acc_no):
        self.name = name
        self.acc_no = acc_no
        self.balance = 0.0
        
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("amount deposited successfully.✅")
        else:
            print("Invailed amount.😒")
            
    def withdraw (self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawal successfully..✅")
        else:
            print("iNSUFFICIENT BALANCE..😒")
            
    def cheak_balance(self):
        print(f"current balance is {self.balance}")
        
    def display(self):
        print("------Account Detail------")
        print("name: ",self.name)
        print("Account Number: ",self.acc_no)
        print("balance: ",self.balance)
        
#main program.
print("🏦🏦WELCOME TO BANK MANAGEMENT SYSTEM 🏦🏦")

name = input("enter your name: ")
acc_no = input("enter your account number: ")

account = Bankaccount(name,acc_no)

while True:
    print("1. Deposite")
    print("2. withdrawal")
    print("3. cheak balance")
    print("4. account detail")
    print("5. exit")
    
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        amount = float(input("enter Deposite amount: "))
        account.deposit(amount)
        
    elif choice == 2:
        amount = float(input("enter your withdrawal amount: "))
        account.withdraw(amount)
        
    elif choice == 3:
        account.cheak_balance()
        
    elif choice == 4:
        account.display()
        
    elif choice == 5:
        print("thaku for using bank management system.🙏🙏")
        break
    else:
        print("Invailed choice! try again")