class automaticTellerMachine(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    
    def balanceEnquiry(self):
        print("your balance is 200$")

    def cashWithdrawl(self):
        balance = 200
        withdrawnAmount = int(input("Enter the amount to be withdrawn - "))
        remainingAmount = balance - withdrawnAmount
        
        if(withdrawnAmount>200):
            print("Your expectations are high, your balance isn't that enough :(")
            withdrawnAmount = int(input("Enter the amount to be withdrawn - "))
        elif(withdrawnAmount<0):
            print("Enter a valid number sir..")
            withdrawnAmount = int(input("Enter the amount to be withdrawn - "))
        elif(withdrawnAmount==0):
            print("Were you here to pass your time..")
            withdrawnAmount = int(input("Enter the amount to be withdrawn - "))
        elif(withdrawnAmount<200):
            remainingAmount = balance - withdrawnAmount
            print("You withdrew " + str(withdrawnAmount) + "$ ,your remaining amount is " + str(remainingAmount) + "$")
            
introString = print("Welcome to ATM")
name = input("What is your name - ")
helloString = print("Hello " + name)

atm = automaticTellerMachine(123456, 1234)

enterActivity = int(input("Enter (1) for viewing your balance ; enter (2) for withdrawing money - "))

if(enterActivity==1):
    atm.balanceEnquiry()
elif(enterActivity==2):
    atm.cashWithdrawl()