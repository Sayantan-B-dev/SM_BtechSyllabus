print("=" * 50)
print("     ATM TRANSACTION SIMULATOR - STUDENT")
print("=" * 50)

pin = input("Enter PIN: ")
if pin != "1234":
    print("Access Denied!")
    exit()

balance = 5000
history = []

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. History")
    print("5. Exit")
    ch = input("Choice: ")

    if ch == '1':
        print(f"Balance: Rs.{balance:.2f}")
        history.append(f"Checked Bal: Rs.{balance:.2f}")

    elif ch == '2':
        amt = float(input("Amount: "))
        balance += amt
        print(f"Deposited Rs.{amt:.2f}")
        history.append(f"Deposit: Rs.{amt:.2f}")

    elif ch == '3':
        amt = float(input("Amount: "))
        if amt > 5000:
            print("Max Rs.5000 per transaction!")
        elif amt > balance:
            print("Insufficient balance!")
        else:
            balance -= amt
            print(f"Withdrawn Rs.{amt:.2f}")
            history.append(f"Withdraw: Rs.{amt:.2f}")

    elif ch == '4':
        print("\n--- Last 10 Transactions ---")
        for t in history[-10:]:
            print(t)

    elif ch == '5':
        print("Thank you!")
        break
