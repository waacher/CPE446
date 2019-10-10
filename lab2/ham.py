# CPE 446 Lab 2
# 7-4 Hamming Code

import numpy

# Returns string of 7 bits
# Input: Number up to 15 (4 bits)
def encode(x):
    assert x < 0b10000, "Value to be encoded is greater than 4 bits"

    x = bin(x)[2:]
    p1 = int(x[0]) ^ int(x[1]) ^ int(x[3])
    p2 = int(x[1]) ^ int(x[2]) ^ int(x[3])
    p3 = int(x[1]) ^ int(x[2]) ^ int(x[3])
    
    result = (p1 << 6) | (p2 << 5) | (int(x[0]) << 4) | (p3 << 3) | (int(x[1]) << 2) | (int(x[2]) << 1) | int(x[3])
   
    return format(result, '#09b')[2:]


# Decodes a string of 7 bits
def decode(x):
    assert int(x, 2) < 0b10000000, "Value to be decoded is greater than 7 bits"
    
    P1_BITS = 0b1101
    P2_BITS = 0b1011
    P3_BITS = 0b0111

    bits = [int(bit) for bit in x]
    
    check = (bits[0] ^ bits[2] ^ bits[4] ^ bits[6])
    check |= ((bits[1] ^ bits[2] ^ bits[5] ^ bits[6]) << 1)
    check |= ((bits[3] ^ bits[4] ^ bits[5] ^ bits[6]) << 2)

    check = int(check)

    if (check == 0):
        return x[2] + x[4] + x[5] + x[6]
    else: 
        err = check
        print("Error at: " + str(err-1))  
        bits[check-1] = bits[check-1] ^ 1
        out_pos = [2,4,5,6]
        n_bits = numpy.array(bits)
        return ''.join(map(str, n_bits[out_pos]))
    
if __name__ == '__main__':

    option = input("Press 'e' to encode or 'd' to decode: ")

    if (option == 'e'):
        e_word = input("\nEnter value to encode: ")
        print(encode(int(e_word)))
    
    elif (option == 'd'):
        d_word = input("\nEnter value to decode: ")
        print(decode(d_word))
