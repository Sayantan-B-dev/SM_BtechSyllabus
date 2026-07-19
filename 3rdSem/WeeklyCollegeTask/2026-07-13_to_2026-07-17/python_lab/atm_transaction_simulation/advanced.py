users = {
    "alice": {"pin": "1111", "bal": 10000, "log": []},
    "bob":   {"pin": "2222", "bal": 20000, "log": []}
}

print("=" * 50)
print("     ATM TRANSACTION SIMULATOR - ADVANCED")
print("=" * 50)

uid = input("User ID: ")
if uid not in users:
    print("Unknown user!")
    exit()

for attempt in range(3, 0, -1):
    pin = input("PIN: ")
    if pin == users[uid]["pin"]: break
    print(f"Wrong! {attempt - 1} tries left")
else:
    print("Account locked!")
    exit()

u = users[uid]

while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Exit")
    ch = input("Choice: ")

    if ch == '1':
        print(f"Balance: Rs.{u['bal']:.2f}")
        u["log"].append(f"Bal: Rs.{u['bal']:.2f}")

    elif ch == '2':
        amt = float(input("Amount: "))
        u["bal"] += amt
        u["log"].append(f"Dep: Rs.{amt:.2f}")
        print("Done")

    elif ch == '3':
        amt = float(input("Amount: "))
        if amt > min(5000, u["bal"]):
            print("Exceeds limit or insufficient balance!")
        else:
            u["bal"] -= amt
            u["log"].append(f"W/D: Rs.{amt:.2f}")
            print("Done")

    elif ch == '4':
        print("\n--- Mini Statement ---")
        for t in u["log"][-5:]:
            print(t)

    elif ch == '5':
        with open("atm_data.txt", "w") as f:
            for uid, data in users.items():
                f.write(f"{uid},{data['pin']},{data['bal']}\n")
        print("Goodbye!")
        break
