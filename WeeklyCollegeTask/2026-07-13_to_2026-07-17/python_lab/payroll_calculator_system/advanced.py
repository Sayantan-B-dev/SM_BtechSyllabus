def calc(basic):
    hra = basic * 0.20
    da = basic * 0.15
    gross = basic + hra + da
    bonus = 5000 if gross > 30000 else 2000
    pf = gross * 0.08
    return hra, da, gross, bonus, pf, gross + bonus - pf

while True:
    print("=" * 50)
    print("     PAYROLL CALCULATOR SYSTEM - ADVANCED")
    print("=" * 50)
    dept = input("Department (or 'quit'): ")
    if dept.lower() == 'quit': break
    name = input("Employee Name: ")
    basic = float(input("Basic Salary: "))

    hra, da, gross, bonus, pf, net = calc(basic)

    print("\n" + "=" * 50)
    print(f"  PAY SLIP - {dept.upper()}")
    print("=" * 50)
    print(f"  Name   : {name}")
    print(f"  Basic  : Rs.{basic:.2f}")
    print(f"  HRA    : Rs.{hra:.2f}")
    print(f"  DA     : Rs.{da:.2f}")
    print(f"  Bonus  : Rs.{bonus:.2f}")
    print(f"  PF     : Rs.{pf:.2f}")
    print("=" * 50)
    print(f"  NET    : Rs.{net:.2f}")
    print("=" * 50)

    with open("payroll.txt", "a") as f:
        f.write(f"{dept},{name},{basic},{net:.2f}\n")
    input("\nPress Enter...")
