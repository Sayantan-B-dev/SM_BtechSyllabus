# =====================================================
#  LIBRARY MANAGEMENT SYSTEM  (menu-driven project)
#  Add / View / Issue / Return / Search books
# =====================================================

WIDTH = 100

BANNER = r"""
██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  
███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
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
BOOKS = {}

# ---------- LIBRARY FUNCTIONS ----------
def add_book(book_id, title, author):
    BOOKS[book_id] = {
        "title": title,
        "author": author,
        "status": "Available",
        "issued_to": "",
    }

def issue_book(book_id, member):
    if book_id in BOOKS and BOOKS[book_id]["status"] == "Available":
        BOOKS[book_id]["status"] = "Issued"
        BOOKS[book_id]["issued_to"] = member
        return True
    return False

def return_book(book_id):
    if book_id in BOOKS and BOOKS[book_id]["status"] == "Issued":
        BOOKS[book_id]["status"] = "Available"
        BOOKS[book_id]["issued_to"] = ""
        return True
    return False

def search_book(term):
    term = term.lower()
    matches = []
    for book_id, book in BOOKS.items():
        if term in book_id.lower() or term in book["title"].lower() or term in book["author"].lower():
            matches.append(book_id)
    return matches

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Library Management System".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] Add Book",
            "  [2] View All Books",
            "  [3] Issue Book",
            "  [4] Return Book",
            "  [5] Search Book",
            "  [6] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "1":
            book_id = input("> Enter book ID: ").strip().upper()
            if book_id in BOOKS:
                print()
                print_boxed(["ERROR: Book ID already exists."])
                print()
                continue
            title = input("> Enter book title: ").strip()
            author = input("> Enter author name: ").strip()
            add_book(book_id, title, author)
            print()
            print_boxed([
                "BOOK ADDED:",
                "",
                f"  Book ID : {book_id}",
                f"  Title   : {title}",
                f"  Author  : {author}",
                f"  Status  : Available"
            ])
            print()

        elif option == "2":
            if not BOOKS:
                print()
                print_boxed(["No books in the library yet."])
                print()
                continue
            lines = [f"  {'ID':<12}{'Title':<30}{'Author':<20}{'Status':<15}{'Issued To':<15}",
                     "-" * (WIDTH - 8)]
            for book_id, book in BOOKS.items():
                lines.append(f"  {book_id:<12}{book['title']:<30}{book['author']:<20}{book['status']:<15}{book['issued_to']:<15}")
            print()
            print_boxed(lines)
            print()

        elif option == "3":
            book_id = input("> Enter book ID: ").strip().upper()
            if book_id not in BOOKS:
                print()
                print_boxed(["ERROR: Book not found."])
                print()
                continue
            if BOOKS[book_id]["status"] != "Available":
                print()
                print_boxed(["ERROR: Book is already issued."])
                print()
                continue
            member = input("> Enter member name: ").strip()
            issue_book(book_id, member)
            print()
            print_boxed([
                "BOOK ISSUED:",
                "",
                f"  Book ID : {book_id}",
                f"  Title   : {BOOKS[book_id]['title']}",
                f"  Issued to: {member}"
            ])
            print()

        elif option == "4":
            book_id = input("> Enter book ID: ").strip().upper()
            if return_book(book_id):
                print()
                print_boxed([f"Book {book_id} returned. Now Available."])
                print()
            else:
                print_boxed(["ERROR: Book not found or not issued."])
                print()

        elif option == "5":
            term = input("> Enter search term (ID/title/author): ").strip()
            matches = search_book(term)
            if not matches:
                print()
                print_boxed(["No books matched your search."])
                print()
                continue
            lines = ["SEARCH RESULTS:", ""]
            for book_id in matches:
                book = BOOKS[book_id]
                lines.append(f"  {book_id} | {book['title']} | {book['author']} | {book['status']}")
            print()
            print_boxed(lines)
            print()

        elif option == "6":
            print()
            print_boxed(["Goodbye!"])
            print()
            break

        else:
            print_boxed(["Invalid option, try again."])
            print()

if __name__ == "__main__":
    main()