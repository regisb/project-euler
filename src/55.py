import euler

def reverse(number):
    digits = euler.digits(number)
    reversed_digits = list(reversed(digits))
    return euler.make_number(reversed_digits)

def is_palindrome(number):
    return number == reverse(number)

def lychrel_degree(number):
    degree = 0
    while degree < 50:
        number += reverse(number)
        degree += 1
        if is_palindrome(number):
            return degree
    return degree

if __name__ == "__main__":
    print lychrel_degree(47)
    print lychrel_degree(4994)
    lychrel_degrees = map(lychrel_degree, range(1, 10000))
    print len(filter(lambda degree: degree >= 50, lychrel_degrees))
