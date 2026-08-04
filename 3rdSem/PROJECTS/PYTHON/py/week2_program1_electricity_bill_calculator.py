# =====================================================
#  ELECTRICITY BILL CALCULATOR  (menu-driven project)
# =====================================================

WIDTH = 100

BANNER = r"""
███████╗██╗     ███████╗ ██████╗████████╗██████╗ ██╗ ██████╗██╗████████╗██╗   ██╗
██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
█████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║██║     ██║   ██║    ╚████╔╝ 
██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║██║     ██║   ██║     ╚██╔╝  
███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║██║╚██████╗██║   ██║      ██║   
╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝   ╚═╝      ╚═╝
██████╗ ██╗██╗     ██╗     
██╔══██╗██║██║     ██║     
██████╔╝██║██║     ██║     
██╔══██╗██║██║     ██║     
██████╔╝██║███████╗███████╗
╚═════╝ ╚═╝╚══════╝╚══════╝
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
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

# ---------- BILL CALCULATION ----------
UNIT = 0
FINAL_BILL = 0
DISCOUNT_RATE = 10
FIXED_CHARGE = 50
USERNAME = ""

ALL_DATA = {}

def savedata(username, unit, final_bill):
    ALL_DATA[username] = f"Unit is {unit}, Final bill is {final_bill}"

def calc(unit):
    bill = 0
    discount = 0
    charge = FIXED_CHARGE

    if unit <= 100:
        bill = unit * 1.5
    elif unit <= 200:
        bill = (100 * 1.5) + ((unit - 100) * 2.5)
    elif unit <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((unit - 200) * 4.0)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + ((unit - 300) * 6.0)

    if bill > 1000:
        discount = DISCOUNT_RATE

    amount_after_discount = bill - (bill * discount) / 100

    final_bill = amount_after_discount + charge

    return final_bill

# ---------- MENU ----------
def main():
    global UNIT, FINAL_BILL, USERNAME

    print(BANNER)
    print("      Terminal Electricity Bill Calculator".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Calculate Bill",
            "  [2] Display Bill Status",
            "  [3] Show All User Info",
            "  [4] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "1":
            username = input("> Enter your name: ").strip()
            try:
                unit = float(input("> Enter the unit amount: ").strip())
            except ValueError:
                print_boxed(["ERROR: Invalid unit amount."])
                print()
                continue
            final_bill = calc(unit)
            UNIT = unit
            FINAL_BILL = final_bill
            USERNAME = username
            savedata(USERNAME, UNIT, FINAL_BILL)
            print()
            print_boxed([
                "BILL CALCULATED:",
                "",
                f"  Final bill for {unit} unit(s) is: {final_bill}"
            ])
            print()

        elif option == "2":
            print()
            print_boxed([
                "BILL STATUS:",
                "",
                f"  Hello {USERNAME}.",
                f"  Your unit is {UNIT}.",
                f"  Discount rate is {DISCOUNT_RATE} (10% for bills more than 1000).",
                f"  Fixed charge is {FIXED_CHARGE}.",
                f"  Your final bill is {FINAL_BILL}."
            ])
            print()

        elif option == "3":
            if not ALL_DATA:
                print()
                print_boxed(["No user data available yet."])
                print()
            else:
                lines = ["ALL USER INFO:", ""]
                for key, value in ALL_DATA.items():
                    lines.append(f"  {key}: {value}")
                print()
                print_boxed(lines)
                print()

        elif option == "4":
            print()
            print_boxed(["Thank you for using the program!"])
            print()
            break

        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()
