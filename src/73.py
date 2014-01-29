import eratosthenes
from math import ceil, floor

def count_fractions_in_range(max_denominator):
    divisors = []
    count = 0
    eratosthenes.init(max_denominator)
    for denominator, denominator_divisors in enumerate(eratosthenes.iter_prime_divisors()):
        divisors.append(denominator_divisors)
        if denominator < 4:
            continue
        min_numerator = int(ceil(denominator/3.))
        max_numerator = int(floor(denominator/2.))
        for numerator in range(min_numerator, max_numerator + 1):
            fraction = float(numerator) / denominator
            if fraction > 1./3 and fraction < 1./2:
                numerator_divisors = divisors[numerator]
                common_divisors = numerator_divisors.intersection(denominator_divisors)
                if len(common_divisors) == 0:
                    #print numerator, denominator
                    count += 1
    return count

if __name__ == "__main__":
    print count_fractions_in_range(12000)

