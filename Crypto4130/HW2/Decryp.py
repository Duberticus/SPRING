#keys in Binary converted using one of those websites
k16 = "100010110001111001001011101010001111001110100001"
k15 = "101110111001110110000111010011010011011010110011"

#got lazy, ChatGpt formatted this
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]
#expands the subkeys from 48 bits to 56 bits
def subkeys2Bigkeys(subKey):
    CD = ['?'] * 56
 
    for i, pos in enumerate(PC2):
        CD[pos-1] = subKey[i]
    return CD

k16 = subkeys2Bigkeys(k16)
#print(k16)
k15 = subkeys2Bigkeys(k15)
#print(k15)

def bruteForce(k16, k15):
    c16 = k16[:28]
    d16 = k16[28:]

    #move C and D of R16 to the previous state which is R15 and match
    c16_rotateR = [c16[-1]] + c16[:-1]
    d16_rotateR = [d16[-1]] + d16[:-1]
    #print(c16)
    #print(c16_rotateR)
    toCmp = c16_rotateR + d16_rotateR

    crackKey = []
    for i in range(56):
        bit15 = k15[i]
        bit16 = k16[i]

        if bit15 != '?':
            crackKey.append(bit15) # Use bit from K15 if we have it
        elif bit16 != '?':
            crackKey.append(bit16) # If K15 was '?', fill it with shifted K16 bit
        else:
            crackKey.append('0')   # If both are '?', default to 0
    return crackKey# had string before but type error

crackKey = bruteForce(k16,k15)
#print(crackKey)
#11110000011011100011001101011001110000110100011110010010

#ok this is round 15, since round 16 == round 0 shift it to the left agian to get round 16
c15 = crackKey[:28]
d15 = crackKey[28:]
c0 = c15[1:] + [c15[0]]
d0 = d15[1:] + [d15[0]]
cd0 = "".join(c0 + d0)

print(cd0)
#11100000110111000110011010110011100001101000111100100101

#Told ChatGPT "after every 7 digits, add a 0" to format

#1001000100101001011100110100011001011011101111111110110011011001