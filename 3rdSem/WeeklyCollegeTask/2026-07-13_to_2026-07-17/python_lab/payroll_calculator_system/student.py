print("=" * 50)
print("     PAYROLL CALCULATOR SYSTEM - STUDENT")
print("=" * 50)

name = input("Employee Name: ")
basic = float(input("Basic Salary: "))

hra = basic * 0.20
da = basic * 0.15
gross = basic + hra + da
bonus = 5000 if gross > 30000 else 2000
pf = gross * 0.08
net = gross + bonus - pf

print("\n" + "-" * 50)
print(f"  Employee : {name}")
print(f"  Basic    : Rs.{basic:.2f}")
print(f"  HRA      : Rs.{hra:.2f}")
print(f"  DA       : Rs.{da:.2f}")
print(f"  Gross    : Rs.{gross:.2f}")
print(f"  Bonus    : Rs.{bonus:.2f}")
print(f"  PF (8%)  : Rs.{pf:.2f}")
print("-" * 50)
print(f"  NET PAY  : Rs.{net:.2f}")
print("-" * 50)
