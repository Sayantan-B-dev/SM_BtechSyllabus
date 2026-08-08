# =====================================================
#  WORD FREQUENCY COUNTER
# =====================================================

WIDTH = 100

BANNER = r"""
██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗███████╗██████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""

# ---------- BOX DRAWING ----------
def box_top(w=WIDTH):
    return "╔" + "═" * (w - 2) + "╗"

def box_bottom(w=WIDTH):
    return "╚" + "═" * (w - 2) + "╝"

def box_line(text, w=WIDTH):
    pad = max(w - 4 - len(text), 0)
    return f"║ {text}{' ' * pad} ║"

def print_boxed(lines, w=WIDTH):
    print(box_top(w))
    for line in lines:
        print(box_line(line, w))
    print(box_bottom(w))

# ---------- WORD COUNTING ----------
chars_to_remove = [
    ".", ",", "-", "!", "?", ";", ":", "'", '"',
    "(", ")", "[", "]", "{", "}", "@", "#", "$",
    "%", "^", "&", "*", "_", "+", "=", "<", ">",
    "/", "\\", "|", "~", "`"
]

def clean_text(text):
    for char in chars_to_remove:
        text = text.replace(char, " ")
    return text.split(" ")

def counter_words(text):
    word_list = [word for word in clean_text(text) if word != '']
    return len(word_list), word_list

def counter_char(text):
    return len(text)

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Word Frequency Counter".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Count words",
            "  [2] Count characters",
            "  [3] Exit"
        ])
        choice = input("> Enter option: ").strip()

        if choice == "1":
            text = input("> Enter text: ").strip()
            num_of_words, words = counter_words(text)
            print()
            print_boxed([
                f"Total words: {num_of_words}",
                "",
                "Words:",
                ", ".join(words)
            ])
            print()
        elif choice == "2":
            text = input("> Enter text: ").strip()
            num_of_chars = counter_char(text)
            print()
            print_boxed([f"Total characters (including spaces and specials): {num_of_chars}"])
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