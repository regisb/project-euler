import eratosthenes

def bottom_left_corner(spiral_size):
    return spiral_size * spiral_size - 1*(spiral_size - 1)

def top_left_corner(spiral_size):
    return spiral_size * spiral_size - 2*(spiral_size - 1)

def top_right_corner(spiral_size):
    return spiral_size * spiral_size - 3*(spiral_size - 1)

def corner_prime_value_count(spiral_size):
    return len(filter(eratosthenes.is_prime_simple, [top_right_corner(spiral_size), top_left_corner(spiral_size), bottom_left_corner(spiral_size)]))

def first_spiral_with_few_primes():
    spiral_size = 3
    prime_count = 0
    corner_count = 1
    while True:
        prime_count += corner_prime_value_count(spiral_size)
        corner_count += 4
        if prime_count < 0.1 * corner_count:
            return spiral_size
        spiral_size += 2

print first_spiral_with_few_primes()
