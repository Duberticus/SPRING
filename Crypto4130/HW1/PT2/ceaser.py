from collections import Counter

toDo = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"

# count = Counter(toDo)
# total = len(count)
# for char, count in count.most_common():
#     percent = (count/total) * 100
#     print(f"{percent}%")
#     print(f"{char}: {count}")

# 55.55555555555556% 
# t: 10
# 50.0%
# i: 9
# 38.88888888888889%
# x: 7
# 27.77777777777778%
# l: 5
# 27.77777777777778%
# p: 5
# 27.77777777777778%
# a: 5
# 27.77777777777778%
# g: 5
# 22.22222222222222%
# h: 4
# 22.22222222222222%
# w: 4
# 16.666666666666664%
# d: 3
# 11.11111111111111%
# j: 2
# 11.11111111111111%
# c: 2
# 5.555555555555555%
# u: 1
# 5.555555555555555%
# r: 1
# 5.555555555555555%
# k: 1
# 5.555555555555555%
# v: 1
# 5.555555555555555%
# q: 1
# 5.555555555555555%
# s: 1

toDo = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"

for char in toDo:
    new = toDo.replace('t', 'E')# shifted 11 times right or 14 times to the left
    new = new.replace('j', 'U')# shifted 11 times
    new = new.replace('x', 'I')
    new = new.replace('l', 'W')
    new = new.replace('p', 'A')
    new = new.replace('a', 'L')
    new = new.replace('u', 'F')
    new = new.replace('c', 'N')
    new = new.replace('r', 'C')
    new = new.replace('h', 'S')
    new = new.replace('i', 'T')
    new = new.replace('w', 'H')
    new = new.replace('g', 'R')
    new = new.replace('k', 'V')
    new = new.replace('d', 'O')
    new = new.replace('v', 'G')
    new = new.replace('q', 'B')
    new = new.replace('s', 'D')
print(new)
#IFWEALLUNITEWEWILLCAUSETHERIVERSTOSTAINTHEGREATWATERSWITHTHEIRBLOOD

#Techumseh

#Q2

# (2^7)^8 = 2^56 possible combinations.

#b. 56 bits

#Q3:
#5 * x = 1(mod 11)
#45 mod 11 = 4 answer: x = 9

#5 * x  = 1(mod 12)
#25 mod 12 = 1 answer = 5

#5 * x = 1(mod 13)
#5 x 8 = 40. 40 mode 13 = 1 answer = 8

#Q4: