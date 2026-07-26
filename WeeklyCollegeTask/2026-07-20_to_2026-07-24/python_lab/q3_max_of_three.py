# Find the maximum among three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Maximum number is:", largest)

# Sample Output:
# Enter first number: 5
# Enter second number: 9
# Enter third number: 3
# Maximum number is: 9.0
