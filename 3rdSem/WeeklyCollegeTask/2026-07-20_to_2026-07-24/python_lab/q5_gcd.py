# GCD using Euclidean algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD is:", a)

# Sample Output:
# Enter first number: 36
# Enter second number: 60
# GCD is: 12
