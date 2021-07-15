from modules.bank_account import *

account = BankAccount("John ", 500, "personal")
account_2 = BankAccount("James ", 500, "business")

#print(account.holder_name)

#account.holder_name = "Ada"
#print(account.holder_name)



account.pay_monthly_fee()
print(account.balance)

account_2.pay_monthly_fee()
print(account_2.balance)



