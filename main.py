#Bank Operation

class Bank:
    bankName = "Bank Masr"
    Address = "Badrashin"

    # Create Account                                                   # Password
    def __init__(self, userName, userAddress, phoneNumber, nationalID, cardNumber):
        self.userName = userName
        self.userAddress = userAddress
        self.phoneNumber = phoneNumber
        self.nationalID = nationalID
        self.cardNumber = cardNumber
        self.Balance = 0.0
        print(f"Hello {userName} Your Account Creation Successfully")

    def Deposit(self,amount):
        self.Balance += amount
        print(f"{amount} Deposit Successfully")

    def Withdraw(self,amount):
        if amount < self.Balance:
            self.Balance -= amount
            print(f"{amount} Withdraw Successfully")
        else:
            print("Your Balance don't Have Enough money to Withdraw")

    def miniStatement(self):
        print(f"Your Account Have {self.Balance}")




print(f"Welcome {Bank.bankName} Branch {Bank.Address}")
name = input("Enter Your User Name : ")
address = input("Enter Your User Address : ")
PhoneNumber = input("Enter Your User Phone Number : ")
NationalID = input("Enter Your User National ID : ")
CardNumber = int(input("Enter Your User Card Number  : "))

Client = Bank(name, address, PhoneNumber, NationalID, CardNumber)

while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit: \n2.Withdraw: \n3.Minis Statement: \n4.Stop: ')
    option = int(input(' '))
    if option == 1:
        amount = float(input('Enter Deposited amount : '))
        Client.Deposit(amount)

    elif option == 2:
        amount = float(input('Enter Withdraw amount : '))
        Client.Withdraw(amount)

    elif option == 3:
        Client.miniStatement()

    elif option == 4:
        print('Thanks for using Bank Masr.... ')
        break
    else:
        print('Invalid Option plz select Another Option')