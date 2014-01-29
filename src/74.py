from math import factorial
import euler

def digit_factorial_sum(number):
    return sum(map(factorial, euler.digits(number)))

def chain_length(number, numbers_seen=None):
    if numbers_seen is None:
        numbers_seen = set()
    if number in numbers_seen:
        return 0
    numbers_seen.add(number)
    next_number = digit_factorial_sum(number)
    return 1 + chain_length(next_number, numbers_seen)

def count_numbers_with_length_sixty(max_value):
    count = 0
    for number in xrange(1, max_value + 1):
        if chain_length(number) == 60:
            count += 1
        if number % 100000 == 0:
            print number
    return count

if __name__ == "__main__":
    print count_numbers_with_length_sixty(999999)
