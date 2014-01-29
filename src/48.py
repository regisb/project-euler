import eratosthenes
import euler

def find_prime_permutations():
    for prime in eratosthenes.prime_iterator():
        if prime > 1000 and prime < 10000:
            permutations = sorted(euler.digit_permutations(prime))
            prime_permutations = filter(eratosthenes.is_prime, permutations)
            for permutation in prime_permutations:
                period = permutation - prime
                if period > 0:
                    if permutation + period in prime_permutations:
                        print str(prime), str(permutation), str(permutation + period)

find_prime_permutations()
