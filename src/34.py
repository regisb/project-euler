from math import factorial
import euler

def all_digit_factorials():
    factorials = []
    number = 9
    while number < 10000000:
        if sum(map(factorial, euler.digits(number))) == number:
            print number
            factorials.append(number)
        number += 1
    return factorials

if __name__ == "__main__":
    print sum(all_digit_factorials())
