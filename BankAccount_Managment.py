class Bankaccount:
    def __init__(self , balance):
        self._balance = balance
        
    def deposit(self , amount):
        self._balance += amount
        print("Money Deposite" , self._balance)
        
    def withdraw(self , amount):
        if(self._balance >= amount):
            self._balance -= amount
            print("Money Withdraw" , self._balance)
        else:
            print("Insufficient Balance")
        
    def check_balance(self):
        print("Balance chacking" , self._balance)
        
    def exit(self):
        print("Exit")
        
account1 = Bankaccount(25000)
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice :"))
    if(choice == 1):
        amount = int(input("Enter your amount"))
        if(amount <= 0):
            print("Invalid Amount")
        else:
            account1.deposit(amount)
    elif(choice == 2):
        amount = int(input("Enter your amount"))
        if(amount <= 0):
            print("Invalid Amount")
        else:
            account1.withdraw(amount)
    elif(choice == 3):
        account1.check_balance()
    elif(choice == 4):
        account1.exit()
        break
    else:
        print("Invalid choice")
