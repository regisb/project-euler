from eratosthenes import is_prime

for i in range(0, 20):
    print i, is_prime(i)

def find_longest_quadratic_primes(a_max, b_max):
    max_prime_count = 0
    max_prime_product = 0
    for a in range(-a_max+1, a_max):
        for b in range(-b_max, b_max):
            n = 0
            while is_prime(n*n + a*n + b):
                if n + 1 > max_prime_count:
                    max_prime_count = n + 1
                    max_prime_product = a*b
                n += 1
    return max_prime_product

if __name__ == "__main__":
    print find_longest_quadratic_primes(1000, 1000)
