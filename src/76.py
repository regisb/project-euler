def count_additions(target_sum, min_value, max_value):
    count = 0
    for max_value_in_sum in range(min_value, max_value):
        for max_value_count in range(1, target_sum // max_value + 1):
            print target_sum, max_value_in_sum*max_value_count
            count += count_additions(target_sum - max_value_in_sum*max_value_count, min_value, max_value_in_sum)
    return count

if __name__ == "__main__":
    print count_additions(100, 1, 100)
