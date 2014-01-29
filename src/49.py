import eratosthenes

def longest_consecutive_prime_sum(max_value):
    eratosthenes.init(max_value)
    max_sum_term_count = 1
    #max_sum_term_prime = 2
    max_sum = 0
    primes = list(eratosthenes.prime_iterator())
    for start_pos in xrange(1, len(primes)):
        for end_pos in xrange(start_pos + max_sum_term_count, len(primes)):
            primes_in_sum = primes[start_pos:end_pos]
            total_sum = sum(primes_in_sum)
            if total_sum >= max_value:
                break
            if total_sum < max_value and eratosthenes.is_prime(total_sum):
                if end_pos - start_pos > max_sum_term_count:
                    max_sum_term_count = end_pos - start_pos
                    #max_sum_term_prime = primes[start_pos]
                    max_sum = total_sum
                    print total_sum#, max_sum_term_prime, max_sum_term_count, primes_in_sum
    return max_sum

print longest_consecutive_prime_sum(1000000)
