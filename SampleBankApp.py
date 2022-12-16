import sys
class Customer:
    '''Customer class with Bank Operations'''
    bankname='INDIA BANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Total Balance:",self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Balance....Cannot perform withdraw operation.")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance after withdraw:",self.balance)

print("***** Welcome to",Customer.bankname,'*****')
name=input("Enter Your Name:")
c=Customer(name)
while True:
    print("Hello",name,"Welcome to",Customer.bankname)
    print("*^*^*^*^*^*^*^*^*^*^*^^*^*^*^*^*^*^*^**^")
    print("Please Press")
    print('D-Deposit \nW-Withdraw \nE-Exit')
    option=input("Choose Your Option:")

    if option=='D' or option=='d':
        amt=float(input("Please Enter Amount to Deposit:"))
        c.deposit(amt)
    elif option=='W' or option=='w':
        amt=float(input("Please Enter Amount to Withdraw:"))
        c.withdraw(amt)
    elif option=='E' or option=='e':
        print("Thanks for Banking with us.....We hope you enjoyed our services.")
        sys.exit()
    else:
        print('Invalid option....Please enter correct option and try again...')
