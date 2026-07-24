n = 5
for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()

# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
