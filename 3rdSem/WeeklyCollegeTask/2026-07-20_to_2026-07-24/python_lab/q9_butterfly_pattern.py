# Butterfly Pattern

n = 5

# Top half
for i in range(n + 1):
    for _ in range(n - i):
        print("*", end="")
    for _ in range(2 * i):
        print(" ", end="")
    for _ in range(n - i):
        print("*", end="")
    print()

# Bottom half
for i in range(1, n + 1):
    for _ in range(i):
        print("*", end="")
    for _ in range(2 * (n - i)):
        print(" ", end="")
    for _ in range(i):
        print("*", end="")
    print()

# Sample Output:
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
