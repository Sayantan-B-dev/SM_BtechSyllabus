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
def create_account(name, pin, initial_deposit):
    if len(ACCOUNTS) > 0:
        card_no = str(max(int(k) for k in ACCOUNTS.keys()) + 1)
    else:
        card_no = "1001"
    ACCOUNTS[card_no] = {"name": name, "pin": pin, "balance": initial_deposit}
    return card_no

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
            "  [1] Create Account",
            "  [2] Check Balance",
            "  [3] Withdraw Cash",
            "  [4] Deposit Cash",
            "  [5] Change PIN",
            "  [6] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "6":
            print()
            print_boxed(["Goodbye!"])
            print()
            break

        if option == "1":
            name = input("> Enter account holder name: ").strip()
            pin = input("> Set a 4-digit PIN: ").strip()
            if not (pin.isdigit() and len(pin) == 4):
                print_boxed(["ERROR: PIN must be exactly 4 digits."])
                print()
                continue
            try:
                initial_deposit = float(input("> Enter initial deposit: ").strip())
                if initial_deposit < 0:
                    raise ValueError
            except ValueError:
                print_boxed(["ERROR: Initial deposit must be a valid non-negative amount."])
                print()
                continue
            card_no = create_account(name, pin, initial_deposit)
            print()
            print_boxed([
                "ACCOUNT CREATED:",
                "",
                f"  Card holder : {name}",
                f"  Card number : {card_no}",
                f"  PIN         : {pin}",
                f"  Balance     : {initial_deposit}"
            ])
            print()
            continue

        if option not in ["2", "3", "4", "5"]:
            print_boxed(["Invalid option, try again."])
            print()
            continue

        card_no = input("> Enter card number: ").strip()
        pin = input("> Enter PIN: ").strip()

        if not authenticate(card_no, pin):
            print_boxed(["ERROR: Invalid card number or PIN."])
            print()
            continue

        if option == "2":
            print()
            print_boxed([
                "BALANCE:",
                "",
                f"  Card holder : {ACCOUNTS[card_no]['name']}",
                f"  Balance     : {ACCOUNTS[card_no]['balance']}"
            ])
            print()

        elif option == "3":
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

        elif option == "4":
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

        elif option == "5":
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