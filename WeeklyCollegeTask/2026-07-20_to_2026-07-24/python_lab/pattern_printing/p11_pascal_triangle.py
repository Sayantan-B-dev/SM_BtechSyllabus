n = 5
for i in range(n):
    print(" " * (n - i - 1) * 2, end="")
    val = 1
    for j in range(i + 1):
        print(val, end="   ")
        val = val * (i - j) // (j + 1)
    print()

#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1
