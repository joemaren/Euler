def multiples():
    number_range = [x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0]
    print(sum(number_range))
multiples()
