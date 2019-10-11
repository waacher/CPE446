# CPE 446 Lab 2
# Parity bit

# Takes an int and adds a parity bit onto the binary representation
def add_parity(n):
    parity = 0
    x = n
    while x:
        parity^= 1
        x = x & (x-1)
    
    return bin(n << 1 | parity)[2:]

# Takes an int and decodes the parity bit at the end
# Returns the string result (and error message if error)
def decode_parity(n):
    x = [int(z) for z in bin(n)[2:]]
    print("Input: " + ''.join(map(str, x)))
    parity = 0
    
    for bit in x:
        parity ^= bit

    if (parity == 0):
        return bin(n)[2:-1]
    else:
        print("Error detected - Faulty word")
        return bin(n)[2:-1]

if __name__ == '__main__':
    #print(add_parity(5))
    print(decode_parity(4))

