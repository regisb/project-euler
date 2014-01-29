import eratosthenes

if __name__ == "__main__":
    abundant_numbers = []
    eratosthenes.init(28123)
    for number, divisors in enumerate(eratosthenes.iter_proper_divisors()):
        if number > 0:
            if sum(divisors) > number:
                abundant_numbers.append(number)

    print abundant_numbers[:30]

    abundant_sums = set()
    for i in range(0, len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            abundant_sums.add(abundant_sum)

    non_abundant_sums = set(range(1, 28124)).difference(abundant_sums)
    print list(abundant_sums)[:30]
    print list(non_abundant_sums)[:30]
    print sum(non_abundant_sums)
