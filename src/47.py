
# DOESN'T WORK!
#import eratosthenes
#from collections import defaultdict
#class PrimeFactorDecomposer(object):
    #_instance = None

    #def __init__(self):
        #self._prime_factors = []

    #@staticmethod
    #def instance():
        #if PrimeFactorDecomposer._instance is None:
            #PrimeFactorDecomposer._instance = PrimeFactorDecomposer()
        #return PrimeFactorDecomposer._instance

    #@staticmethod
    #def decompose(number):
        #return PrimeFactorDecomposer.instance().decomposition(number)

    #def decomposition(self, number):
        #self._ensure_size(number + 1)
        #if self._prime_factors[number] is None:
            #self._prime_factors[number] = self._decomposition(number)
        #return self._prime_factors[number]

    #def _ensure_size(self, size):
        #if len(self._prime_factors) < size:
            #self._prime_factors += [None]*(size - len(self._prime_factors))

    #def _decomposition(self, number):
        #for divisor in eratosthenes.prime_iterator():
            #if number == divisor or number < divisor:
                #return defaultdict(int, {number: 1})
            #if number % divisor == 0:
                #decomposition = self.decomposition(number // divisor)
                #decomposition[divisor] += 1
                #return decomposition

#def prime_factors(number):
    #return PrimeFactorDecomposer.decompose(number)


def iter_prime_factors():
    max_value = 1000000
    prime_factors = [[], [1]]
    while len(prime_factors) < max_value + 1:
        prime_factors.append([])
    for number in xrange(2, max_value + 1):
        if len(prime_factors[number]) == 0:
            # number is prime
            for multiplier in range(2, max_value // number):
                prime_factors[number * multiplier].append(number)
        yield prime_factors[number]


def find_four_distinct_prime_factors_number():
    count = 0
    for number, prime_factors in enumerate(iter_prime_factors()):
        if len(prime_factors) == 4:
            count += 1
        else:
            count = 0
        if count == 4:
            return number - 3

if __name__ == "__main__":
    #print prime_factors(644)
    #print prime_factors(645)
    #print prime_factors(646)
    print find_four_distinct_prime_factors_number()
