def fibonacci():
    """Return the sum of all even numbers less than 4,000,000 in the Fibonacci sequence"""
    sum = 0
    a, b = 1, 1

    while a < 4000000:
        if a % 2 == 0:
            sum += a
        a, b = a + b, a
    print(sum)

fibonacci()


