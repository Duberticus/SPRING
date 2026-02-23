
path = "B:/Crypto4130/HW1/cipher.txt"

s = 'abcdefghijklmnopqrstuvwxyz ".,;-\''

with open(file = path ,encoding = 'utf-8', mode = "r") as f:
    toCount = f.read()

    counts = {char: 0 for char in s}

    for c in toCount:
        if c in counts:
         counts[c] += 1

    #totalCar = 3896
    for char, count in counts.items():
        totalPerc = int(count)/3896
        print(totalPerc)
        print(f"{repr(char)}: {count}")

# totalCar = 3896
# 'a': 125 - 3%
# 'b': 41 - 1%
# 'c': 1 - 0.2% 
# 'd': 47 - 1.2%
# 'e': 50 - 1.2%
# 'f': 42 - 1.1 %
# 'g': 168 - 4.3% could be C or S or L but  shows up 41 times and LL is more common than CC and SS g -> L
# 'h': 54 - 1.4% possibly B
# 'i': 5 - 0.1%
# 'j': 50 - 1.2% likely a consenant
# 'k': 352 - 9% cannot be A since aa is not common in english T possibly wikipedia says its at 9.1% and TT is likely to happen 3 times so k -> T(not sure)
# 'l': 103 - 2.6%
# 'm': 81 - 2%
# 'n': 6 - 0.2%
# 'o': 7 - 0.2%
# 'p': 1 - 0.02%
# 'q': 224 - 5.7%
# 'r': 175 - 4.5%
# 's': 369 - 9.5% A,I possibly 
# 't': 53 - 1.3%
# 'u': 19 - 0.5%
# 'v': 75 - 2.0% Y, W maybe
# 'w': 33 - 0.8%
# 'x': 207 - 5.3% L,C possibly
# 'y': 6 - 0.15% Q,J
# 'z': 230 - 6.0%
# ' ': 99 - 2.5%
# '"': 219 - 5.6%
# ',': 75 - 1.9%
# '-': 272 - 7% A,I,O based on internet probably O since its the closest to 7%
# '.': 645 - 16% probably spaces!!!
# ';': 62 - 1.6%

#Highest frquency
#E T A O I N S H R D L U
#percentage
#https://www.rd.com/article/common-letters-english-language/#:~:text=The%20top%20ten%20most%20common%20letters%20in,L%20%E2%80%93%205.4893%25%20*%20C%20%E2%80%93%204.5388%25
#https://en.wikipedia.org/wiki/Letter_frequency

# E – 11.1607%
# A – 8.4966%
# R – 7.5809%
# I – 7.5448%
# O – 7.1635%
# T – 6.9509%
# N – 6.6544%
# S – 5.7351%
# L – 5.4893%
# C – 4.5388%


#common doubles
# ss ee tt ff ll mm oo

#original cypher has 
# 'gg' shown up 41 times? most likely LL
# 'dd' shows up 4 times? 
# 'kk' shows up 3 times 
# 'll' shows up 2 times 
# 'qq' is 2 times tt is once 
# 'xx' is shown up 13 times
#'zz' shown up 2 times

