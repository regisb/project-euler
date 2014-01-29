import eratosthenes
from math import sqrt

def smallest_goldbach_fail(max_value):
    sieve = [True]*(max_value+1)
    for prime in eratosthenes.prime_iterator():
        if prime >= max_value:
            break
        max_square = int(sqrt(0.5*(max_value - prime))) + 1
        for square in xrange(1, max_square):
            number = prime + 2*square*square
            if number > max_value:
                break
            sieve[number] = False
    for number in range(3, max_value+1, 2):
        if not eratosthenes.is_prime(number):
            if sieve[number]:
                return number

if __name__ == "__main__":
    print smallest_goldbach_fail(100000)
