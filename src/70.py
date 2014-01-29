import eratosthenes
import euler

def sorted_digits(number):
    return sorted(euler.digits(number))

def are_permutations(x, y):
    return sorted_digits(x) == sorted_digits(y)

def permutable_min_totient(max_value):
    eratosthenes.init(max_value)

    min_relative_totient = 1000000
    min_relative_totient_number = 0
    for number, prime_divisors in enumerate(eratosthenes.iter_prime_divisors()):
        if number < 2:
            continue
        totient = number
        # See http://en.wikipedia.org/wiki/Euler%27s_totient_function
        for prime_divisor in prime_divisors:
            totient *= 1 - 1./prime_divisor
        totient = int(totient)
        if are_permutations(number, totient):
            relative_totient = float(number)/totient
            if relative_totient < min_relative_totient:
                min_relative_totient = relative_totient
                min_relative_totient_number = number
                print min_relative_totient, min_relative_totient_number
    return min_relative_totient_number

print permutable_min_totient(10000000)
