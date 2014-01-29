import eratosthenes

if __name__ == "__main__":
    eratosthenes.init(9999)

    total_sum = 0
    divisors = []
    for number, div in enumerate(eratosthenes.iter_proper_divisors()):
        divisors.append(div)
        if len(divisors) == 10000:
            break

        # Does number have a friend?
        sum_div = sum(div)
        if sum_div < number:
            if sum(divisors[sum_div]) == number:
                total_sum += number + sum_div
    print total_sum
