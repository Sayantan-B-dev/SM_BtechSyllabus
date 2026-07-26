n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
for i in range(2, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# A B C D E
# A B C D
# A B C
# A B
# A
# A B
# A B C
# A B C D
# A B C D E
