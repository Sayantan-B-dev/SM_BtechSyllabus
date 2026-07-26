n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(n - j, end=" ")
        else:
            print(" ", end=" ")
    print()

# 5       1
#   4   2
#     3
#   2   4
# 1       5
