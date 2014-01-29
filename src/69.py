import eratosthenes

def max_totient_number(max_value):
    eratosthenes.init(max_value)

    #divisors = []
    max_relative_totient = 0
    max_relative_totient_number = 0
    for number, prime_divisors in enumerate(eratosthenes.iter_prime_divisors()):
        #divisors.append(prime_divisors)
        if number < 2:
            continue
        if number%100000 == 0: print number
        totient = number
        relative_totient = 0
        # See http://en.wikipedia.org/wiki/Euler%27s_totient_function
        for prime_divisor in prime_divisors:
            totient *= 1 - 1./prime_divisor
        relative_totient = float(number)/totient
        #for coprimer in xrange(1, number):
            #if len(divisors[coprimer].intersection(prime_divisors)) == 0:
                #totient += 1
                #relative_totient = float(number)/totient
                ##if relative_totient <= max_relative_totient:
                    ##break
        #print max_relative_totient, max_relative_totient_number, relative_totient
        if relative_totient > max_relative_totient:
            max_relative_totient = relative_totient
            max_relative_totient_number = number
    return max_relative_totient_number

print max_totient_number(1000000)
