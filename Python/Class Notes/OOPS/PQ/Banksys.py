class Accounts:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    def debit(self,amount):
        self.balance -= amount
        print("amount",amount,"Was debited from",self.acc_no)      
    
    def credit(self,amount):
        self.balance += amount
        print("amount",amount,"Was credited in",self.acc_no)
    def show_balance(self):
        print(self.balance)

a1 = Accounts(96000,94)
a1.credit(4000)   
a1.debit(64000)
a1.show_balance()    

    
