from math import sqrt

MAX_VALUE = 10000000

def init(max_value):
    global MAX_VALUE
    MAX_VALUE = max_value

PRIMALITY_SIEVE = None
def _init_primality_sieve():
    global PRIMALITY_SIEVE
    PRIMALITY_SIEVE = [True] * (MAX_VALUE + 1)
    PRIMALITY_SIEVE[0] = False
    PRIMALITY_SIEVE[1] = False
    number = 2
    while number <= MAX_VALUE:
        if PRIMALITY_SIEVE[number]:
            multiple = number * 2
            while multiple <= MAX_VALUE:
                PRIMALITY_SIEVE[multiple] = False
                multiple += number
        number += 1

def _check_sieve_is_init():
    if PRIMALITY_SIEVE is None:
        _init_primality_sieve()

def is_prime(n):
    _check_sieve_is_init()
    return PRIMALITY_SIEVE[n]

def is_prime_simple(number):
    divisor = 2
    max_divisor = int(sqrt(number))
    while divisor < max_divisor:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def is_prime_fastest(number):
    if number <= MAX_VALUE:
        return is_prime(number)
    else:
        return is_prime_simple(number)

def prime_iterator():
    _check_sieve_is_init()
    for number, primality in enumerate(PRIMALITY_SIEVE):
        if primality:
            yield number

def next_prime(number):
    next_number = number + 1
    while True:
        if PRIMALITY_SIEVE[next_number]:
            return next_number
        next_number += 1

def prime_range(start, end):
    _check_sieve_is_init()
    number = start
    while number < end:
        if PRIMALITY_SIEVE[number]:
            yield number
        number += 1

def iter_divisors():
    """iter_divisors
    Iterator over divisors of a number:

        for number, divisors in enumerate(iter_divisors()):
            print number, divisors

        This function yields integer arrays that are the divisors of any given
        number. It uses a method inspired by the sieve of Eratosthenes and it's
        quite fast. It runs in O(max_value) to find all divisors for all numbers
        less or equal to max_size.
    """
    divisors = []
    while len(divisors) < MAX_VALUE + 1: divisors.append([])

    # 0 has no divider
    yield divisors[0]

    number = 1
    while number <= MAX_VALUE:
        multiple = number
        while multiple <= MAX_VALUE:
            divisors[multiple].append(number)
            multiple += number
        yield divisors[number]
        number += 1

def divisors_simple(number):
    if number == 0:
        return []
    return filter(lambda divisor: number%divisor == 0, range(1, number/2)) + [number]

def iter_proper_divisors():
    for divisors in iter_divisors():
        yield divisors[:-1]

def iter_prime_divisors():
    """iter_prime_divisors
    Iterate over the prime divisors of numbers from 0 to MAX_VALUE.
    E.g: prime_divisors(6) = set([2, 3])
         prime_divisors(7) = set([7])
    """
    divisors = []
    while len(divisors) < MAX_VALUE + 1: divisors.append(set())
    number = 0
    while True:
        if number > 1:
            if len(divisors[number]) == 0:
                for multiple in range(number, MAX_VALUE + 1, number):
                    divisors[multiple].add(number)
        yield divisors[number]
        number += 1
        if number > MAX_VALUE:
            break

def iter_totient():
    totients = range(0, MAX_VALUE + 1)
    for number, prime_divisors in enumerate(iter_prime_divisors()):
        if number < 2:
            yield 0
            continue
        if len(prime_divisors) == 1 and number in prime_divisors:
            # See http://en.wikipedia.org/wiki/Euler%27s_totient_function
            for multiple in range(number, MAX_VALUE + 1, number):
                totients[multiple] *= 1 - 1./number
        yield int(totients[number])
