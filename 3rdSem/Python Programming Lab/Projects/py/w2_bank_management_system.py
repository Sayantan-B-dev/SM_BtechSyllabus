# =====================================================
#  BANK MANAGEMENT SYSTEM  (menu-driven project)
#  Create / Deposit / Withdraw / Check Balance
# =====================================================

import math
import random

WIDTH = 100

BANNER = r"""
██████╗  █████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝
██████╔╝███████║██╔██╗ ██║█████╔╝ 
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ 
██████╔╝██║  ██║██║ ╚████║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
"""

# ---------- BOX DRAWING ----------
def box_top(w=WIDTH):
    return "+" + "-" * (w - 2) + "+"

def box_bottom(w=WIDTH):
    return "+" + "-" * (w - 2) + "+"

def box_divider(w=WIDTH):
    return "+" + "-" * (w - 2) + "+"

def box_line(text, w=WIDTH):
    pad = max(w - 4 - len(text), 0)
    return f"| {text}{' ' * pad} |"

def print_boxed(lines, w=WIDTH):
    print(box_top(w))
    for line in lines:
        print(box_line(line, w))
    print(box_bottom(w))

# ---------- DATA ----------
USERS = {"A2291274298": {'name': 'sayantan', 'pin': '1234', 'balance': 10000}}
ACCOUNTS = ["A2291274298"]

# ---------- BANK FUNCTIONS ----------
def generate_account():
    while True:
        num = math.floor(random.random() * (10 ** 10))
        account_no = "A" + str(num)
        if account_no not in ACCOUNTS:
            return account_no

def create_account(name, pin):
    account_no = generate_account()
    USERS[account_no] = {"name": name, "pin": pin, "balance": 0}
    ACCOUNTS.append(account_no)
    return account_no

def authenticate(account, pin):
    if account in USERS and USERS[account]['pin'] == pin:
        return True
    return False

def deposit(account, amount):
    USERS[account]['balance'] += amount

def withdraw(account, amount):
    if amount <= USERS[account]['balance']:
        USERS[account]['balance'] -= amount
        return True
    return False

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Bank Management System".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Create an Account",
            "  [2] Check Balance",
            "  [3] Withdraw Money",
            "  [4] Deposit Money",
            "  [5] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "1":
            name = input("> Enter your name: ").strip()
            pin = input("> Enter security PIN: ").strip()
            account_no = create_account(name, pin)
            print()
            print_boxed([
                "ACCOUNT CREATED:",
                "",
                f"  Account number : {account_no}",
                f"  Account holder : {name}",
                f"  Initial balance: 0"
            ])
            print()

        elif option == "2":
            account = input("> Enter account number: ").strip()
            if account not in ACCOUNTS:
                print()
                print_boxed(["ERROR: Please create your account first."])
                print()
                continue
            pin = input("> Enter your PIN: ").strip()
            if authenticate(account, pin):
                print()
                print_boxed([
                    "BALANCE:",
                    "",
                    f"  Account holder : {USERS[account]['name']}",
                    f"  Account balance: {USERS[account]['balance']}"
                ])
                print()
            else:
                print_boxed(["ERROR: Invalid account number or PIN."])
                print()

        elif option == "3":
            account = input("> Enter account number: ").strip()
            if account not in ACCOUNTS:
                print()
                print_boxed(["ERROR: Please create your account first."])
                print()
                continue
            pin = input("> Enter your PIN: ").strip()
            if authenticate(account, pin):
                try:
                    amount = float(input("> Enter amount to withdraw: ").strip())
                except ValueError:
                    print_boxed(["ERROR: Invalid amount."])
                    print()
                    continue
                if withdraw(account, amount):
                    print()
                    print_boxed([
                        "WITHDRAWAL SUCCESSFUL:",
                        "",
                        f"  New balance: {USERS[account]['balance']}"
                    ])
                    print()
                else:
                    print()
                    print_boxed(["ERROR: Insufficient balance."])
                    print()
            else:
                print_boxed(["ERROR: Invalid account number or PIN."])
                print()

        elif option == "4":
            account = input("> Enter account number: ").strip()
            if account not in ACCOUNTS:
                print()
                print_boxed(["ERROR: Please create your account first."])
                print()
                continue
            pin = input("> Enter your PIN: ").strip()
            if authenticate(account, pin):
                try:
                    amount = float(input("> Enter amount to deposit: ").strip())
                except ValueError:
                    print_boxed(["ERROR: Invalid amount."])
                    print()
                    continue
                deposit(account, amount)
                print()
                print_boxed([
                    "DEPOSIT SUCCESSFUL:",
                    "",
                    f"  New balance: {USERS[account]['balance']}"
                ])
                print()
            else:
                print_boxed(["ERROR: Invalid account number or PIN."])
                print()

        elif option == "5":
            print()
            print_boxed(["Goodbye!"])
            print()
            break

        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()
