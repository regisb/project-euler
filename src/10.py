import eratosthenes

total_sum = 0
for prime in eratosthenes.prime_iterator():
    if prime > 2000000:
        break
    total_sum += prime
print total_sum

