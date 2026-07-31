# =====================================================
#  SIMPLE XOR + BASE64 ENCRYPTION  (no huge numbers)
# =====================================================

import base64

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

# ---------- ENCRYPTION (XOR + Base64) ----------
KEY = 0x9e3779b9  # fixed key (you can change it)

def encrypt(text):
    # XOR each char with a rotating key (byte-wise)
    enc_bytes = bytearray()
    key_bytes = KEY.to_bytes(4, 'big')
    for i, ch in enumerate(text):
        enc_bytes.append(ord(ch) ^ key_bytes[i % 4])
    # Encode to Base64 for a clean, compact string
    return base64.b64encode(bytes(enc_bytes)).decode()

def decrypt(encoded):
    # Decode Base64, then XOR back
    enc_bytes = base64.b64decode(encoded)
    dec_chars = []
    key_bytes = KEY.to_bytes(4, 'big')
    for i, b in enumerate(enc_bytes):
        dec_chars.append(chr(b ^ key_bytes[i % 4]))
    return ''.join(dec_chars)

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Encryption (XOR + Base64)".center(WIDTH))
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