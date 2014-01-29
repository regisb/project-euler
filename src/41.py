import euler
import eratosthenes


def largest_pandigital_number(digit_count):
    number = euler.make_number(range(1, digit_count + 1))
    permutations = euler.digit_permutations(number)
    permutations.sort(reverse=True)
    for permutation in permutations:
        if eratosthenes.is_prime_simple(permutation):
            return permutation
    return None

if __name__ == "__main__":
    for size in range(9, -1, -1):
        pandigital = largest_pandigital_number(size)
        if pandigital is not None:
            print pandigital
            exit(0)
