def cycle_length(q):
    if q%2 == 0 or q%5 == 0:
        return 0
    for cycle_length in range(1, q+1):
        if (10**cycle_length - 1) % q == 0:
            return cycle_length

if __name__ == "__main__":
    print max(cycle_length(q) for q in range(2, 1000))
    #max_cycle_length = 0
    #for q in range(2, 1000):
        #if q%2 == 0 or q%5 == 0:
            #continue
        ## Find cycle length, which is necessarily less than q
        #for cycle_length in range(1, q+1):
            #if (10**cycle_length - 1) % q == 0:
                #break
        #max_cycle_length = max(cycle_length, max_cycle_length)
    #print max_cycle_length
