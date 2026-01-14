balance=5000

def withdraw_money(amount):
    global balance
    if amount<=0:
        raise ValueError("The ammount should be greater than 0 ")
    if amount>balance:
        raise RuntimeError("Insufficient balance")
    
    balance -=amount
    return balance

try:
    print("Welcome to the ATM")

    user_input=input("ENter amount to withdraw:")
    amount=float(user_input)

    remaining_balance=withdraw_money(amount)
    print(f"Withdrawal successful!")
    print(f"Remaining balance:{remaining_balance}")

    print(f"Remaining balance: ₹{remaining_balance}")

except ValueError as ve:
    print("Input Error:",ve)

except RuntimeError as re:
    print("Transaction Error:", re)

except Exception as e:
    print("Unexpected Error occurred.")

else:
    print("Transaction completed without errors.")

finally:
    print("\n--- SESSION CLOSED ---")