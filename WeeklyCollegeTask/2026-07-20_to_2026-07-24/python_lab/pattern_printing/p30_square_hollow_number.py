n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# 1 2 3 4 5
# 1       5
# 1       5
# 1       5
# 1 2 3 4 5
