class Account:
    def __init__(self,name,email):
        self.name =name
        self.email=email
        self.balance=0
    def printAccount(self):
        print self.name+''+self.email+'balance:'+str(self.balance)
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount

acc1=Account('testaccount','test@gmail.com')
print acc1.name
print acc1.email
print 'deposite 2000'
acc1.deposite(2000)
acc1. printAccount()
print 'withdraw 500rs'
acc1.withdraw(500)
acc1.printAccount()










































