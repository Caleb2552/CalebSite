class ATM:
    def __init__(self):
        self.balance = 0

        def check_balance(self):
            print(f"Your balance is: ${self.balance}")

        def deposit(self, amount):
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is: ${self.balance}")

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. Your new balance is: ${self.balance}")
            else:
                print("Insufficient funds")            

def main():
    atm = ATM()

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount you wish to deposit"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount you wish to withdraw"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice")                  
