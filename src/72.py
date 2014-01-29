import eratosthenes

def sum_totients(max_value):
    eratosthenes.init(max_value)
    total = 0
    for number, totient in enumerate(eratosthenes.iter_totient()):
        total += totient
        if number >= max_value:
            return total

if __name__ == "__main__":
    #print sum_totients(8)
    print sum_totients(1000000)


