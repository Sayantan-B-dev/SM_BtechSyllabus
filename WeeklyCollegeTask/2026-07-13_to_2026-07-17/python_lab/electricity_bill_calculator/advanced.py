def calc(units):
    if units <= 100: return 1.5
    elif units <= 200: return 2.5
    elif units <= 300: return 4.0
    return 6.0

while True:
    print("=" * 50)
    print("   ELECTRICITY BILL CALCULATOR - ADVANCED")
    print("=" * 50)
    name = input("Customer Name (or 'quit'): ")
    if name.lower() == 'quit': break
    units = float(input("Units Consumed: "))

    rate = calc(units)
    charge = units * rate
    fixed = 50
    total = charge + fixed
    disc = total * 0.05 if total > 1000 else 0
    gst = (total - disc) * 0.18
    grand = total - disc + gst

    print("\n" + "=" * 50)
    print(f"  BILL - {name.upper()}")
    print("=" * 50)
    print(f"  Units        : {units}")
    print(f"  Rate         : Rs.{rate:.2f}/unit")
    print(f"  Energy Chg   : Rs.{charge:.2f}")
    print(f"  Fixed Chg    : Rs.{fixed:.2f}")
    print(f"  Discount     : Rs.{disc:.2f}")
    print(f"  GST (18%)    : Rs.{gst:.2f}")
    print("=" * 50)
    print(f"  GRAND TOTAL  : Rs.{grand:.2f}")
    print("=" * 50)

    with open("bills.txt", "a") as f:
        f.write(f"{name},{units},{grand:.2f}\n")
    input("\nPress Enter...")
