class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction = []
    
    def transaction_history(self):
        if not self.transaction:
            print("No Transactions Found!")
        else:
            print(f"-------{self.name}'s Transaction history--------------")
            for i, transaction in enumerate(self.transaction, 1):
                print(f"{i}) {transaction}")
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def check_balance(self):
        print(f"{self.name}'s balance: {self.balance} ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds.")
        else:
            self.balance -= amount
            self.transaction.append(f"Withdrawn {amount}")
            print(f"Withdrawn {amount}. New Balance: {self.balance}")
    
def main():
    print("-------WELCOME TO DEMO BANK--------")
    name = input("Enter your name: ")
    balance = float(input("Enter opening balance: "))
    account = BankAccount(name, balance)

    while True:
        choice = input("<-----CHOOSE AN OPTION----->\n 1. DEPOSIT\n 2. WITHDRAW\n 3. CHECK BALANCE\n 4. TRANSACTION HISTORY\n 5.EXIT > " )

        if choice == "1":
            amount = float(input("Enter amount: "))
            account.deposit(amount)
            
        elif choice == "2":
            amount = float(input("Enter amount: "))
            account.withdraw(amount)
          
        elif choice == "3":
            account.check_balance()
    
        elif choice == "4":
            account.transaction_history()
        
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Enter a valid input.")

main()


            

            

