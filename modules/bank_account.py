#class is the blueprint to create an object, an object is what the item actually is

class BankAccount: 
    # the holder_name/ balance/ type 
    # on line 4 is the same is the = holder_name/balance/type below
    # dont mix up with self.holder_name/balance/type
    # (holder_name, balance, type) are local variables
    def __init__(self, holder_name, balance, type):
       
        # instance variable = self.holder_name
        self.holder_name = holder_name
        self.balance = balance
        self.type = type
        self._rates = {
            "personal": 10,
            "business": 50,
            "savings": 10
        }

    # This is a method 
    def pay_in(self, amount):
        self.balance += amount

    def pay_monthly_fee(self):
            self.balance -= self._rates[self.type]

    
       




    



    

