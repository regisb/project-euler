def champernowne():
    representation = ""
    for number in range(1, 1000000):
        representation += str(number)
    product = 1
    for pos in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        print(representation[pos - 1])
        product *= int(representation[pos - 1])
    return product

print(champernowne())

