def count_combinations(total_sum, coins):
    if total_sum == 0:
        return 1
    if len(coins) == 0:
        return 0
    count = 0
    biggest_coin_value = coins[0]
    biggest_coin_count = 0
    while biggest_coin_count*biggest_coin_value <= total_sum:
        count += count_combinations(total_sum -  biggest_coin_count*biggest_coin_value,
                                    coins[1:])
        biggest_coin_count += 1
    return count

if __name__ == "__main__":
    #print count_combinations(200, [200, 100])
    print count_combinations(200, [200, 100, 50, 20, 10, 5, 2, 1])
