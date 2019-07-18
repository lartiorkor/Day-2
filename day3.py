#dictionaries
acct_1 = {"first_name": "Kwame", "last_name" : "Asante", "account_type" : "fixed deposit", "balance" : 80}
balance = acct_1.get(balance)

acct_2 = {"first_name": "Joshua", "last_name" : "Badu", "account_type" : "student", "balance" : 64}

acct_3 = {"first_name": "Francisca", "last_name" : "Clems", "account_type" : "savings", "balance" : 27}


#dictionary of dictionaries
dict { "00001": "acct_1", "00002": "acct_2"}

#list of dictionaries
l[acct_1, acct_2]

l2[a, b, c]


#dictionary of lists
dict{"a": "l", "b": "l2"}



def deposit(amount_to_deposit, balance):
    return amount_to_deposit + balance

one = deposit(20,balance)

print(one)



def withdrawal(amount_to_withdraw, balance):
     return amount_to_withdraw - balance
    
two = withdrawal(50, balance)

print (two)

