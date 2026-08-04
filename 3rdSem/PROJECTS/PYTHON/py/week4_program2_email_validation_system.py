# =====================================================
#  EMAIL VALIDATION SYSTEM  (styled with ASCII boxes)
# =====================================================

WIDTH = 100

BANNER = r"""
███████╗███╗   ███╗ █████╗ ██╗██╗     
██╔════╝████╗ ████║██╔══██╗██║██║     
█████╗  ██╔████╔██║███████║██║██║     
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
 ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
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

# ---------- VALIDATION FUNCTIONS ----------
def name_check(name):
    # Allow only letters and digits (no spaces, dots, special chars)
    if not name:
        return False
    for ch in name:
        if not ch.isalnum():
            return False
    return True

def domain_check(domain):
    # Must have exactly one dot, and only letters/digits before and after
    if domain.count('.') != 1:
        return False
    local, tld = domain.split('.')
    if not local or not tld:
        return False
    # Both parts must be alphanumeric
    if not local.isalnum() or not tld.isalnum():
        return False
    # TLD must be at least 2 characters (common TLDs)
    if len(tld) < 2:
        return False
    return True

def email_checker(email):
    # Basic checks
    if '@' not in email:
        return "Email must contain '@'."
    if ' ' in email:
        return "Email cannot contain spaces."
    if len(email) < 11:
        return "Email should be at least 11 characters long."
    if email.count('@') > 1:
        return "There should be only one '@' in an email."

    local, domain = email.split('@', 1)

    # Validate local part
    if not name_check(local):
        return "Invalid local part (only letters and digits allowed)."

    # Validate domain
    if not domain_check(domain):
        return "Invalid domain (must have exactly one dot, and only letters/digits)."

    # Additional check: TLD must be one of common ones
    tld = domain.split('.')[1]
    valid_tlds = {"com", "org", "edu", "net", "gov", "mil"}
    if tld.lower() not in valid_tlds:
        return f"Invalid TLD '{tld}' – must be one of {', '.join(valid_tlds)}."

    return "The email is Valid!"

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Email Validation System".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Check Email",
            "  [2] Exit"
        ])
        choice = input("> Enter option: ").strip()

        if choice == "1":
            email = input("> Enter your email address: ").strip()
            result = email_checker(email)
            print()
            print_boxed(["RESULT:", "", result])
            print()
        elif choice == "2":
            print()
            print_boxed(["Goodbye!"])
            print()
            break
        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()
