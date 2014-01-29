def is_valid(gon):
    if 10 in gon[:5]:
        return False
    total = gon[5] + gon[0] + gon[1]
    if gon[6] + gon[1] + gon[2] != total:
        return False
    if gon[7] + gon[2] + gon[3] != total:
        return False
    if gon[8] + gon[3] + gon[4] != total:
        return False
    if gon[9] + gon[4] + gon[0] != total:
        return False
    return True

def gon_representation(gon):
    exterior_value = min(gon[5:])
    exterior_index = gon.index(exterior_value)
    representation = ""
    for _ in range(0, 5):
        interior_index1 = (exterior_index - 5) % 5
        interior_index2 = (exterior_index - 4) % 5
        representation += str(gon[exterior_index]) + str(gon[interior_index1]) + str(gon[interior_index2])

        exterior_index += 1
        if exterior_index == 10:
            exterior_index = 5
        exterior_value = gon[exterior_index]
    return int(representation)

def iter_gon_representation():
    numbers = range(1, 11)
    numbers_used = [False]*10
    for gon in _iter_gon(numbers, numbers_used):
        if is_valid(gon):
            yield gon_representation(gon)

def _iter_gon(numbers, numbers_used):
    if all(numbers_used):
        yield []
        raise StopIteration

    for number_index, number in enumerate(numbers):
        if not numbers_used[number_index]:
            numbers_used[number_index] = True
            for partial_gon in _iter_gon(numbers, numbers_used):
                yield [number] + partial_gon
            numbers_used[number_index] = False

def maximum_gon():
    max_representation = 0
    for gon_representation in iter_gon_representation():
        if gon_representation > max_representation:
            max_representation = gon_representation
            print max_representation
    return max_representation

if __name__ == "__main__":
    print maximum_gon()
