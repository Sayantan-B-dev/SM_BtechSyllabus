# Reverse a 2-digit number

num = int(input("Enter a 2-digit number: "))

ones = num % 10
tens = num // 10

reversed_num = ones * 10 + tens

print("Reversed number:", reversed_num)

# Sample Output:
# Enter a 2-digit number: 47
# Reversed number: 74
