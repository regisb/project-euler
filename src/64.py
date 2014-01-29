import continued

if __name__ == "__main__":
    #print continued_fraction_period(23)
    #print continued_fraction_period(13)

    odd_period_count = 0
    for number in range(1, 10001):
        period = continued.fraction_period(number)
        if period % 2 == 1:
            odd_period_count += 1
    print odd_period_count
