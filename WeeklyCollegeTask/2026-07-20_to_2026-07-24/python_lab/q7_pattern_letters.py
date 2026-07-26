# Letter Pattern

n = 4

for i in range(n):
    letter = chr(65 + i)
    row = (letter + " ") * (n - i)
    print("  " * i + row.rstrip())

# Sample Output:
# A A A A
#   B B B
#     C C
#       D
