#CA 00 01 F0 03 11 01 2C CD = 202 0 1 240 3 11 1 44
#CA 00 01 F0 02 01 2C DF=202 0 1 240 2 1 44
def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n
sum=202+0+1+240+3+11+1+44
CD=~sum
mask = 0b111111111
print(bin(sum ^ mask))
print(bin(sum))
#print(bin(bit_not(sum)))