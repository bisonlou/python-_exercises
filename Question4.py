def get_bank_balance(transaction_log):
    balance = 0
    for key, amount in transaction_log.items():
        if key =='D':
            balance += amount
        elif key == 'W':
            balance -= amount
    return balance

if __name__ == "__main__":
    input_count = int(input("Enter number of transactions : "))

    transaction_log ={}
    for i in range(input_count):
        transaction = input("Enter transaction").split()
        key = str(transaction[0])
        amount = int(transaction[1])

        transaction_log[key] = amount
    
    print(get_bank_balance(transaction_log))


