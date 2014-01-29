import continued
from math import sqrt

def solve_diophantine(D):
    """solve_diophantine
    This is hard for D=61. Funny enough, the particular case of 61 is noted by
    Wikipedia: http://en.wikipedia.org/wiki/Pell%27s_equation

    Brahmagupta's method looks great, but Lagrange's method with continued
    fractions even better:
    http://www-history.mcs.st-andrews.ac.uk/HistTopics/Pell.html
    :param D:
    """
    if sqrt(D) == int(sqrt(D)):
        return None, None

    #print "---------"
    decomposition, period = continued.fraction_decomposition_one_period(D)
    if period % 2 == 0:
        # References: http://www.math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf
        # But also:
        # http://www-history.mcs.st-andrews.ac.uk/HistTopics/Pell.html
        # (although the Lagrange method looks wrong because they don't make the
        # distinction whether the period is even or odd.)
        numerator, denominator = continued.fraction_partial_value_of(D, period)
    else:
        numerator, denominator = continued.fraction_partial_value_of(D, 2*period)
    #print "D:", D, "decomposition:", decomposition, "period:", period, (numerator, denominator)
    return numerator, denominator

if __name__ == "__main__":
    max_x = 0
    max_D = 0
    for D in range(1, 1001):
        x, y = solve_diophantine(D)
        if x is not None and y is not None:
            result = x*x - D*y*y - 1
            if result != 0:
                print "HOUSTON!", D
            if x > max_x:
                max_x = x
                max_D = D
    print max_D, max_x
