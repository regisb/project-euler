#! /usr/bin/env python

def is_prime(n):
    if n == 1 or n == 2:
        return True
    for divider in range(2, n):
        if n%divider == 0:
            return False
    return True

def nth_prime_number(nth):
    count = 0
    number = 1
    while count < nth:
        number += 1
        if is_prime(number):
            count += 1
    return number

def erathosthene_nth_prime_number(nth):
    MAX_SIZE = 1000000
    primality = [True]*MAX_SIZE
    prime_count = 0
    for candidate in range(2, MAX_SIZE + 1):
        if primality[candidate - 1]:
            prime_count += 1
            if prime_count == nth:
                return candidate
        pos = candidate * 2 - 1
        while pos < MAX_SIZE:
            primality[pos] = False
            pos += candidate

if __name__ == "__main__":
    #print nth_prime_number(10001)
    print erathosthene_nth_prime_number(10001)
