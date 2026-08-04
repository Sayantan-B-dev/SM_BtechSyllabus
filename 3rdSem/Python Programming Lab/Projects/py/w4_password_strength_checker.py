# =====================================================
#  PASSWORD STRENGTH CHECKER  (styled with ASCII boxes)
# =====================================================

SPECIAL_CHARS = "!@#$%^&*()"
WIDTH = 100

BANNER = r"""
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝
███████╗████████╗██████╗ ███████╗███╗   ██╗ ██████╗████████╗██╗  ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║  ██║
███████╗   ██║   ██████╔╝█████╗  ██╔██╗ ██║██║  ███╗  ██║   ███████║
╚════██║   ██║   ██╔══██╗██╔══╝  ██║╚██╗██║██║   ██║  ██║   ██╔══██║
███████║   ██║   ██║  ██║███████╗██║ ╚████║╚██████╔╝  ██║   ██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
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

# ---------- VALIDATION FUNCTIONS ----------
def password_validator(password):
    has_num = any(ch.isdigit() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_special = any(ch in SPECIAL_CHARS for ch in password)
    long_enough = len(password) >= 8

    checks = {
        "At least 8 characters": long_enough,
        "Contains a number": has_num,
        "Contains a lowercase letter": has_lower,
        "Contains an uppercase letter": has_upper,
        f"Contains a special character ({SPECIAL_CHARS})": has_special,
    }

    if not long_enough:
        return "weak", "Password needs to have at least 8 characters.", checks
    if has_num and has_lower and has_upper and has_special:
        return "strong", "Password is Strong! Good to go.", checks
    elif has_num and has_lower:
        return "medium", "Try adding an uppercase letter and a special character.", checks
    else:
        return "weak", "Add a mix of numbers, lowercase, uppercase & special chars.", checks

STRENGTH_LABEL = {"strong": "STRONG [***]", "medium": "MEDIUM [**-]", "weak": "WEAK [*--]"}

def print_result(strength, message, checks, w=WIDTH):
    label = STRENGTH_LABEL[strength]
    filled = list(checks.values()).count(True)
    total = len(checks)
    bar_len = w - 10
    filled_len = int(bar_len * filled / total)
    bar = "#" * filled_len + "-" * (bar_len - filled_len)

    print()
    print(box_top(w))
    print(box_line(f"RESULT: {label}", w))
    print(box_divider(w))
    print(box_line(f"[{bar}] {filled}/{total}", w))
    print(box_line("", w))

    for req, met in checks.items():
        tag = "[OK]" if met else "[NO]"
        print(box_line(f"{tag} {req}", w))

    print(box_divider(w))

    max_msg = w - 6
    words = message.split()
    lines = []
    cur = ""
    for word in words:
        while len(word) > max_msg:
            if cur:
                lines.append(cur)
                cur = ""
            lines.append(word[:max_msg-1] + "-")
            word = word[max_msg-1:]
        if len(cur) + len(word) + 1 > max_msg:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)

    for wline in lines:
        print(box_line(wline, w))

    print(box_bottom(w))
    print()

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Password Strength Checker".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Check Password",
            "  [2] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "1":
            pw = input("> Enter your password: ")
            strength, message, checks = password_validator(pw)
            print_result(strength, message, checks)
        elif option == "2":
            print()
            print_boxed(["Goodbye!"])
            print()
            break
        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()
