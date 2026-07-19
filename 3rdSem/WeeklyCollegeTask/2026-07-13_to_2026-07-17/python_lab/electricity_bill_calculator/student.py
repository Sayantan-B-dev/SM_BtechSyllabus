print("=" * 50)
print("   ELECTRICITY BILL CALCULATOR - STUDENT")
print("=" * 50)

name = input("Customer Name: ")
units = float(input("Units Consumed: "))

if units <= 100: rate = 1.5
elif units <= 200: rate = 2.5
elif units <= 300: rate = 4.0
else: rate = 6.0

charge = units * rate
fixed = 50
total = charge + fixed

if total > 1000:
    disc = total * 0.05
    total -= disc
else:
    disc = 0

print("\n" + "-" * 50)
print(f"Customer   : {name}")
print(f"Units      : {units}")
print(f"Rate       : Rs.{rate:.2f}/unit")
print(f"Charge     : Rs.{charge:.2f}")
print(f"Fixed      : Rs.{fixed:.2f}")
print(f"Discount   : Rs.{disc:.2f}")
print("-" * 50)
print(f"TOTAL BILL : Rs.{total:.2f}")
print("-" * 50)
