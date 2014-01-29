import euler

n = 1
while True:
    number = n*(2*n - 1)
    if euler.is_pentagonal(number):
        print number
    n += 1
