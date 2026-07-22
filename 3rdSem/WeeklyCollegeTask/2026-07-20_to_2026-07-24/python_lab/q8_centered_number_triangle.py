# Centered Number Triangle

n = 3

for i in range(n):
    num = i + 1
    spaces = (n - i - 1) * 2

    print(" " * spaces, end="")

    for j in range(2 * i + 1):
        print(num, end=" ")

    print()

# Sample Output:
#     1
#   2 2 2
# 3 3 3 3 3
