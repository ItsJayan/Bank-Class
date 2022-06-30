from tracemalloc import start


class atm(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit
    def incard(self):
        print("insert credit card")
    def outcard(self):
        print("take your card out")
    def account(self):
        print("choose current or savings")
    def pin(self):
        print("put your pin")
Bank=atm("bank","small","bankofbaroda",100)
print(Bank.incard())
print(Bank.account())
print(Bank.pin())
print(Bank.outcard())
