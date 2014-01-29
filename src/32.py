import euler

def product_is_pandigital(a, b):
    digit_included = [False]*10
    digit_count = 0
    for number in [a, b, a*b]:
        for digit in euler.digits(number):
            digit_count += 1
            if digit == 0 or digit_included[digit]:
                return False
            digit_included[digit] = True
    return digit_count == 9

def all_pandigital_products():
    pandigital_products = set()
    for a in range(1, 10000):
        for b in range(a+1, 10000):
            if product_is_pandigital(a, b):
                print a, b, a*b
                pandigital_products.add(a*b)
            if euler.digit_count(a) + euler.digit_count(b) + euler.digit_count(a*b) > 9:
                break
    return pandigital_products

if __name__ == "__main__":
    print euler.digits(123456789)
    print product_is_pandigital(39, 187)
    print sum(all_pandigital_products())

