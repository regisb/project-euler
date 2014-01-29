import eratosthenes
import euler

def concatenated(candidate, prime):
    return euler.make_number(euler.digits(candidate) + euler.digits(prime))

concatenable_cache = {}
def are_concatenable(candidate, prime):
    global concatenable_cache
    if candidate not in concatenable_cache:
        concatenable_cache[candidate] = {}
    answer = concatenable_cache[candidate].get(prime)
    if answer is not None:
        return answer
    answer = eratosthenes.is_prime_fastest(concatenated(candidate, prime)) and \
            eratosthenes.is_prime_fastest(concatenated(prime, candidate))
    concatenable_cache[candidate][prime] = answer
    return answer

def are_concatenable_with(candidate, *primes):
    for prime in primes:
        if not are_concatenable(candidate, prime):
            return False
    return True

def prime_pair_sets(max_value):
    eratosthenes.init(max_value)
    min_sum = 1000000000
    best_primes = None
    for prime1 in eratosthenes.prime_range(2, max_value):
        if prime1 > min_sum:
            break
        for prime2 in eratosthenes.prime_range(2, prime1):
            if are_concatenable_with(prime2, prime1):
                for prime3 in eratosthenes.prime_range(2, prime2):
                    if are_concatenable_with(prime3, prime1, prime2):
                        for prime4 in eratosthenes.prime_range(2, prime3):
                            if are_concatenable_with(prime4, prime1, prime2, prime3):
                                for prime5 in eratosthenes.prime_range(2, prime4):
                                    if are_concatenable_with(prime5, prime1, prime2, prime3, prime4):
                                        primes = (prime1, prime2, prime3, prime4, prime5)
                                        prime_sum = sum(primes)
                                        if prime_sum < min_sum:
                                            print primes, prime_sum
                                            min_sum = prime_sum
                                            best_primes = primes
    return best_primes

primes = prime_pair_sets(10000)
print primes, sum(primes)

