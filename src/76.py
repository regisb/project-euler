#! /usr/bin/env python
import eratosthenes

def main():
    problem78()
    problem77()
    problem76()

def problem78():
    # Problem 78
    n = 1
    previous_values = [0, 1]
    current_values = []
    while True:
        n += 1
        for p in range(n, 0, -1):
            current_values[p] = previous_values[p]

        n += 1
        values.append(None)

    max_n = 10000
    Results.values = big_table(max_n)
    print "Problem 78:"
    for n in range(1, max_n):
        for p in range(n, 0, -1):
            count = count_additions(n, p)
        print n, count
        if count % 1000000 == 0:
            print "    solution:", n
            break
    print "done"

def problem77():
    PrimeResults.values = big_table(101)
    eratosthenes.init(110)
    n = 3
    while True:
        result = count_prime_additions(n, 2)
        if eratosthenes.is_prime(n):
            result -= 1
        if result > 5000:
            break
        n += 1
    print "Problem 77:", n

def problem76():
    # Problem 76
    Results.values = big_table(101)
    print "Problem 76:", count_additions(100, 1) - 1


class Results(object):
    values = None

class PrimeResults(object):
    values = None

def count_additions(n, p):
    if n == p:
        return 1
    if n < p:
        return 0
    result = Results.values[n][p]
    if result is not None:
        return result
    result = count_additions(n-p, p) + count_additions(n, p+1)
    Results.values[n][p] = result
    return result

def count_prime_additions(n, p):
    if n == p:
        if eratosthenes.is_prime(n):
            return 1
        return 0
    if n < p:
        return 0
    result = PrimeResults.values[n][p]
    if result is not None:
        return result
    result = count_prime_additions(n-p, p) + count_prime_additions(n, eratosthenes.next_prime(p))
    PrimeResults.values[n][p] = result
    return result

def big_table(size):
    values = [None]*size
    for i in range(0, size):
        values[i] = [None]*size
    return values

if __name__ == "__main__":
    main()
