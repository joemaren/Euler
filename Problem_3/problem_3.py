def largestPrime():
    num = 600851475143
    factors = []

    for i in range(1, num//2):
        if num % i == 0:
            factors.append(i)
    
    print(max(factors))
