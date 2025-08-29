class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
      fix-atm-deposit
        if amount <= 0:

 
        global deposit_history
        if amount <= 0:
 
        if amount >= 0:
 
        main
            print("Amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
 
            deposit_history[count] = self.balance
 

    def withdraw(self, amount):
        global withdraw_history
        if amount <= 0:
            print("Amount must be positive.")
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")
            withdraw_history[count] = self.balance
def main():
    global atm
    current_amnt = int(input("Enter the initial balance of your Account: "))
    atm = ATM(current_amnt)
def both():
    global withdraw_history 
    global deposit_history
    global result
    d=1
    result.update(deposit_history)
    result.update(withdraw_history)
    for i in range(1,len(result)+1):
        if d in result.keys():
            print(f"{d} : {result[d]}")
            d+=1
            

 
withdraw_history = {}
deposit_history = {}
result = {}
count=1
main() 
while True:
    print("************************* ATM Simulator *****************************")
    print("""
          1.Deposit
          2.Withdrawal
          3.Transaction History
          4.Exit
          """)
    print("*********************************************************************")
    n=int(input("Enter your choice: "))
    if n==1:
        a = int(input("Enter the Amount to be Depositted: "))
        atm.deposit(a)
        count+=1
    elif n==2:
        b = int(input("Enter the Amount to be Withdrawn: "))
        atm.withdraw(b)
        count+=1
    elif n==3:
        if withdraw_history == {} and deposit_history == {}:
            print("###NO TRANSACTION HAS BEEN DONE###")
        else:
            print("----------------------------------- Transaction History -------------------")
            print('''
                1.Withdraw History
                2.Deposit History
                3.Both Withdraw and Deposit history''')
            print("---------------------------------------------------------------------------")
            c=int(input("Enter your choice: "))
            if c==1:
                print("When : How Much Amount Withdrawn")
                for i in withdraw_history:
                    print(f"{i} : {withdraw_history[i]}")
            elif c==2:
                print("When : How Much Amount Depositted")
                for i in deposit_history:
                    print(f"{i} : {deposit_history[i]}")
            elif c==3:
                both()
            else:
                print("###INVALID CHOICE###")
    
    elif n==4:
        print("Exiting .....")
        break
    else:
        print("###INVALID CHOICE###")  
 
atm = ATM(1000)
atm.deposit(200)
atm.withdraw(1500)
atm.withdraw(500)
 
