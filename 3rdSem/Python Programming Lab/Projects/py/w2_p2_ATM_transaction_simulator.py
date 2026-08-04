# =====================================================
#  ATM TRANSACTION SIMULATOR  (menu-driven project)
#  Check balance / Withdraw / Deposit / Change PIN
# =====================================================

WIDTH = 100

BANNER = r"""
 █████╗ ████████╗███╗   ███╗
██╔══██╗╚══██╔══╝████╗ ████║
███████║   ██║   ██╔████╔██║
██╔══██║   ██║   ██║╚██╔╝██║
██║  ██║   ██║   ██║ ╚═╝ ██║
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝
████████╗██████╗  █████╗ ███╗   ██╗███████╗ █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗███████║██║        ██║   ██║██║   ██║██╔██╗ ██║
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
███████╗██╗███╗   ███╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██║████╗ ████║██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║██╔████╔██║██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║██║╚██╔╝██║██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║██║██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

# ---------- BOX DRAWING ----------
def box_top(w=WIDTH):
    return "╔" + "═" * (w - 2) + "╗"

def box_bottom(w=WIDTH):
    return "╚" + "═" * (w - 2) + "╝"

def box_divider(w=WIDTH):
    return "╠" + "═" * (w - 2) + "╣"

def box_line(text, w=WIDTH):
    pad = max(w - 4 - len(text), 0)
    return f"║ {text}{' ' * pad} ║"

def print_boxed(lines, w=WIDTH):
    print(box_top(w))
    for line in lines:
        print(box_line(line, w))
    print(box_bottom(w))

# ---------- DATA ----------
ACCOUNTS = {"4091": {"name": "Sayantan", "pin": "1234", "balance": 25000.0}}

MAX_ATTEMPTS = 3

# ---------- ATM FUNCTIONS ----------
def authenticate(card_no, pin):
    if card_no in ACCOUNTS and ACCOUNTS[card_no]["pin"] == pin:
        return True
    return False

def withdraw(card_no, amount):
    if amount <= ACCOUNTS[card_no]["balance"]:
        ACCOUNTS[card_no]["balance"] -= amount
        return True
    return False

def deposit(card_no, amount):
    ACCOUNTS[card_no]["balance"] += amount

def change_pin(card_no, old_pin, new_pin):
    if ACCOUNTS[card_no]["pin"] == old_pin:
        ACCOUNTS[card_no]["pin"] = new_pin
        return True
    return False

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal ATM Transaction Simulator".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Check Balance",
            "  [2] Withdraw Cash",
            "  [3] Deposit Cash",
            "  [4] Change PIN",
            "  [5] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "5":
            print()
            print_boxed(["Goodbye!"])
            print()
            break

        if option not in ["1", "2", "3", "4"]:
            print_boxed(["Invalid option, try again."])
            print()
            continue

        card_no = input("> Enter card number: ").strip()
        pin = input("> Enter PIN: ").strip()

        if not authenticate(card_no, pin):
            print_boxed(["ERROR: Invalid card number or PIN."])
            print()
            continue

        if option == "1":
            print()
            print_boxed([
                "BALANCE:",
                "",
                f"  Card holder : {ACCOUNTS[card_no]['name']}",
                f"  Balance     : {ACCOUNTS[card_no]['balance']}"
            ])
            print()

        elif option == "2":
            try:
                amount = float(input("> Enter amount to withdraw: ").strip())
            except ValueError:
                print_boxed(["ERROR: Invalid amount."])
                print()
                continue
            if amount <= 0:
                print_boxed(["ERROR: Amount must be positive."])
                print()
                continue
            if withdraw(card_no, amount):
                print()
                print_boxed([
                    "WITHDRAWAL SUCCESSFUL:",
                    "",
                    f"  Withdrawn     : {amount}",
                    f"  New balance   : {ACCOUNTS[card_no]['balance']}"
                ])
                print()
            else:
                print()
                print_boxed(["ERROR: Insufficient balance."])
                print()

        elif option == "3":
            try:
                amount = float(input("> Enter amount to deposit: ").strip())
            except ValueError:
                print_boxed(["ERROR: Invalid amount."])
                print()
                continue
            if amount <= 0:
                print_boxed(["ERROR: Amount must be positive."])
                print()
                continue
            deposit(card_no, amount)
            print()
            print_boxed([
                "DEPOSIT SUCCESSFUL:",
                "",
                f"  Deposited     : {amount}",
                f"  New balance   : {ACCOUNTS[card_no]['balance']}"
            ])
            print()

        elif option == "4":
            old_pin = input("> Enter current PIN: ").strip()
            new_pin = input("> Enter new PIN: ").strip()
            if change_pin(card_no, old_pin, new_pin):
                print()
                print_boxed(["PIN CHANGED SUCCESSFULLY."])
                print()
            else:
                print_boxed(["ERROR: Current PIN is incorrect."])
                print()

if __name__ == "__main__":
    main()