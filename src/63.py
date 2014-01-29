from math import log

def find_n_power_with_n_digits():
    n_power_with_n_digits = set()
    iteration_count = 0
    count = 0
    for number in range(1, 10):
        max_power = int(log(10)/(log(10) - log(number)))
        count += max_power
        #continue

        #for power in range(1, max_power + 1):
            #iteration_count += 1
            #if log(number) >= log(10) * (power - 1.)/power:
                #n_power_with_n_digits.add(number**power)
    print count
    return n_power_with_n_digits

n_power_with_n_digits = find_n_power_with_n_digits()
print n_power_with_n_digits, len(n_power_with_n_digits)
