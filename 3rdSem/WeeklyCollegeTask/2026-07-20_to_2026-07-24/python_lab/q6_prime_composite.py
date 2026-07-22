# Check whether a number is prime or composite

n = int(input("Enter a number: "))

if n < 2:
    print(n, "is neither prime nor composite")
else:
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1

    if count == 2:
        print(n, "is Prime")
    else:
        print(n, "is Composite")

# Sample Output:
# Enter a number: 17
# 17 is Prime
