# =====================================================
#  SIMPLE CHARACTER SHIFT ENCRYPTION
# =====================================================

WIDTH = 100

BANNER = r"""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ██████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗██╔══██╗
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██████╔╝
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██╔══██╗
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝
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

# ---------- ENCRYPTION (simple character shift) ----------
SHIFT = 5  # shift amount (you can change it)

def shift(text, amount):
    out = []
    for ch in text:
        code = ord(ch)
        if 32 <= code <= 126:                # shift only printable ASCII
            code = ((code - 32 + amount) % 95) + 32
        out.append(chr(code))
    return ''.join(out)

def encrypt(text):
    return shift(text, SHIFT)

def decrypt(encoded):
    return shift(encoded, -SHIFT)

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Encryption (Character Shift)".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Encrypt text",
            "  [2] Decrypt text",
            "  [3] Exit"
        ])
        choice = input("> Enter option: ").strip()

        if choice == "1":
            text = input("> Enter text to encrypt: ").strip()
            result = encrypt(text)
            print()
            print_boxed(["ENCRYPTED:", "", result])
            print()
        elif choice == "2":
            text = input("> Enter encrypted text: ").strip()
            try:
                dec = decrypt(text)
                print()
                print_boxed(["DECRYPTED:", "", dec])
                print()
            except Exception:
                print_boxed(["ERROR: Invalid encrypted text."])
                print()
        elif choice == "3":
            print()
            print_boxed(["Goodbye!"])
            print()
            break
        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()