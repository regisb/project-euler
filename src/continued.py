from math import sqrt

def fraction_period(square_number):
    """continued_fraction_period
    More or less the algorithm recommended by Wikipedia:
    http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

    :param square_number:
    """
    decomposition, period = fraction_decomposition_one_period(square_number)
    return period

def fraction_decomposition_one_period(square_number):
    auv_values = []
    decomposition = []
    period = 0
    for (a, q, u, v) in iter_fraction_decomposition_full(square_number):
        auv = (a, u, v)
        if auv in auv_values:
            period = len(auv_values) - auv_values.index(auv)
            break
        auv_values.append(auv)
        decomposition.append(a)
    return decomposition, period

def iter_fraction_decomposition(square_number):
    for a, q, u, v in iter_fraction_decomposition_full(square_number):
        yield a

def iter_fraction_decomposition_full(square_number):
    sqrt_number = sqrt(square_number)
    an = int(sqrt_number)
    if an == sqrt_number:
        yield (an, 0, 0, 0)
        raise StopIteration
    qn = 1./(sqrt_number - an)
    un = 1.
    vn = an * 1.
    while True:
        yield (an, qn, un, vn)

        an_next = int(qn)
        un_next = (square_number - vn*vn)/un
        vn_next = (an_next*square_number - vn*(un + an_next*vn))/un
        qn_next = un_next * 1. /(sqrt_number - vn_next)# computing qn otherwise is too imprecise

        an = an_next
        qn = qn_next
        un = un_next
        vn = vn_next


def fraction_partial_value_of(square_number, length):
    decomposition = []
    for component in iter_fraction_decomposition(square_number):
        if len(decomposition) >= length:
            break
        decomposition.append(component)
    return fraction_partial_value(decomposition)

def fraction_partial_value(continued_fraction_decomposition):
    """fraction_partial_value
    This is borrowed from exercise #65

    :param continued_fraction_decomposition:
    """
    if len(continued_fraction_decomposition) == 0:
        return (0, 0)
    if len(continued_fraction_decomposition) == 1:
        return continued_fraction_decomposition[0], 1
    previous_numerator, previous_denominator = fraction_partial_value(continued_fraction_decomposition[1:])
    # a + 1/(p/q)
    numerator = continued_fraction_decomposition[0]*previous_numerator + previous_denominator
    denominator = previous_numerator
    return numerator, denominator
