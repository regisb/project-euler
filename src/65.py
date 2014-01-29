import continued

def e_continued_fraction_decomposition(length):
    if length == 0:
        return []
    decomposition = [2]
    for i in range(0, length - 1):
        if i % 3 == 0 or i % 3 == 2:
            decomposition.append(1)
        else:
            decomposition.append(2*(i//3 + 1))
    return decomposition

if __name__ == "__main__":
    decomposition = e_continued_fraction_decomposition(100)
    numerator, denominator = continued.fraction_partial_value(decomposition)
    print numerator, denominator
    print sum(map(int, str(numerator)))
