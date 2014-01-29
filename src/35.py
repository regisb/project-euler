import euler
import eratosthenes

def is_circular(number):
    if number > 2:
        for digit in euler.digits(number):
            if digit%2 == 0:
                return False
    if not eratosthenes.is_prime(number):
        return False
    for rotation in euler.digit_rotations(number):
        if not eratosthenes.is_prime(rotation):
            return False
    return True

def circular_primes(max_value):
    return filter(is_circular, range(1, max_value))

if __name__ == "__main__":
    max_value = 1000000
    eratosthenes.init(max_value)
    circular_numbers = circular_primes(max_value)
    print circular_numbers, len(circular_numbers)

