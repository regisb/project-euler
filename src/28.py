def spiral_diagonal_sum(spiral_size):
    n = spiral_size
    return n*n*n*2./3 + n*n/2. + n*4./3 - 3./2

    #p = (spiral_size - 1) / 2
    #return 1 + p*26/3. + p*p*10 + p*p*p*16./3
    #return 1 + 4*p + 2*p*(p+1) + p*(p+1)*(2*p+1)*8./3

print spiral_diagonal_sum(3)
print spiral_diagonal_sum(5)
print spiral_diagonal_sum(1001)

