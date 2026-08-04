# =====================================================
#  HOTEL BOOKING SYSTEM  (menu-driven project)
#  View rooms / Book / Check-out / View bookings
# =====================================================

WIDTH = 100

BANNER = r"""
██╗  ██╗ ██████╗ ████████╗███████╗██╗     
██║  ██║██╔═══██╗╚══██╔══╝██╔════╝██║     
███████║██║   ██║   ██║   █████╗  ██║     
██╔══██║██║   ██║   ██║   ██╔══╝  ██║     
██║  ██║╚██████╔╝   ██║   ███████╗███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
██████╗  ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██████╔╝██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██╗██║   ██║██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
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
ROOM_TYPES = {
    "Single": {"price": 1000, "count": 2},
    "Double": {"price": 2000, "count": 2},
    "Suite":  {"price": 5000, "count": 1},
}

BOOKINGS = {}

# ---------- HOTEL FUNCTIONS ----------
def available_rooms(room_type):
    booked = sum(1 for b in BOOKINGS.values() if b["room_type"] == room_type and b["status"] == "Booked")
    return ROOM_TYPES[room_type]["count"] - booked

def book_room(name, room_type, nights):
    if available_rooms(room_type) <= 0:
        return None, f"No {room_type} rooms available."
    booking_id = 1001 + len(BOOKINGS)
    total = ROOM_TYPES[room_type]["price"] * nights
    BOOKINGS[booking_id] = {
        "name": name,
        "room_type": room_type,
        "nights": nights,
        "total": total,
        "status": "Booked",
    }
    return booking_id, total

def checkout(booking_id):
    if booking_id in BOOKINGS and BOOKINGS[booking_id]["status"] == "Booked":
        BOOKINGS[booking_id]["status"] = "Checked-out"
        return True
    return False

# ---------- MENU ----------
def main():
    print(BANNER)
    print("      Terminal Hotel Booking System".center(WIDTH))
    print()

    while True:
        print_boxed([
            "  [1] View Rooms & Availability",
            "  [2] Book a Room",
            "  [3] Check-Out / Free a Room",
            "  [4] View All Bookings",
            "  [5] Exit"
        ])
        option = input("> Enter option: ").strip()

        if option == "1":
            lines = ["AVAILABLE ROOMS:", ""]
            for room_type, info in ROOM_TYPES.items():
                avail = available_rooms(room_type)
                lines.append(f"  {room_type:<8}: Rs.{info['price']}/night  |  Available: {avail}/{info['count']}")
            print()
            print_boxed(lines)
            print()

        elif option == "2":
            name = input("> Enter guest name: ").strip()
            print()
            print_boxed(["SELECT ROOM TYPE:", "",
                         "  Single - Rs.1000/night",
                         "  Double - Rs.2000/night",
                         "  Suite  - Rs.5000/night"])
            room_type = input("> Enter room type: ").strip().capitalize()
            if room_type not in ROOM_TYPES:
                print_boxed(["ERROR: Invalid room type."])
                print()
                continue
            try:
                nights = int(input("> Enter number of nights: ").strip())
                if nights <= 0:
                    raise ValueError
            except ValueError:
                print_boxed(["ERROR: Nights must be a positive number."])
                print()
                continue
            booking_id, result = book_room(name, room_type, nights)
            if booking_id is None:
                print()
                print_boxed([result])
                print()
            else:
                print()
                print_boxed([
                    "ROOM BOOKED:",
                    "",
                    f"  Booking ID  : {booking_id}",
                    f"  Guest       : {name}",
                    f"  Room type   : {room_type}",
                    f"  Nights      : {nights}",
                    f"  Total amount: Rs.{result}"
                ])
                print()

        elif option == "3":
            try:
                booking_id = int(input("> Enter booking ID: ").strip())
            except ValueError:
                print_boxed(["ERROR: Invalid booking ID."])
                print()
                continue
            if checkout(booking_id):
                print()
                print_boxed([f"Booking {booking_id} checked out. Room is now free."])
                print()
            else:
                print_boxed(["ERROR: Booking not found or already checked out."])
                print()

        elif option == "4":
            if not BOOKINGS:
                print()
                print_boxed(["No bookings yet."])
                print()
                continue
            lines = ["ALL BOOKINGS:", ""]
            for bid, b in BOOKINGS.items():
                lines.append(f"  ID {bid}: {b['name']} | {b['room_type']} | {b['nights']} night(s) | Rs.{b['total']} | {b['status']}")
            print()
            print_boxed(lines)
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