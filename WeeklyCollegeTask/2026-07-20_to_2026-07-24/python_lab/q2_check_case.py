# Check whether a character is uppercase, lowercase, or not a letter

ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("It is an UPPERCASE letter")
elif 'a' <= ch <= 'z':
    print("It is a lowercase letter")
else:
    print("Not an alphabet character")

# Sample Output:
# Enter a character: g
# It is a lowercase letter
