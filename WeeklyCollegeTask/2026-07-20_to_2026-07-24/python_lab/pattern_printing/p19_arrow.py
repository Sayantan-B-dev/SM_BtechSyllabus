n = 5
for i in range(1, n):
    print("  " * (n - i - 1) + "* " * i)
print("* " * n)
for i in range(n - 2, 0, -1):
    print("  " * (n - i - 1) + "* " * i)

#       *
#     * *
#   * * *
# * * * *
# * * * * *
#   * * *
#     * *
#       *
