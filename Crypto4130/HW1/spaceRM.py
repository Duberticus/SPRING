path = "B:/Crypto4130/HW1/cpy.txt"

with open(path, encoding = "utf-8", mode = 'r') as file:
    for line in file:
        pH = line.replace(' ', '@')
        new = pH.replace('.', ' ')
        #spaces reveal that s char is a single charactor by itself so it has to be either A or I
        newNew = new.replace('s', 'A') #could be A This is correct DNC
        sNew = newNew.replace('q', 'N') #DNC
        sNew = sNew.replace('a', 'D')
        sNew = sNew.replace("'", 'O')
        sNew = sNew.replace('"', 'I') #DNC
        sNew = sNew.replace("-", "T")
        sNew = sNew.replace("t", "F") #DNC
        sNew = sNew.replace("z", "R")
        sNew = sNew.replace("@", "U") #DNC
        sNew = sNew.replace("x", "S")
        sNew = sNew.replace("k", "E") #DNC
        sNew = sNew.replace("v", "B") #DNC
        sNew = sNew.replace("g", "L")
        sNew = sNew.replace("e", "G")
        sNew = sNew.replace(",", "M")
        sNew = sNew.replace("r", "H")
        sNew = sNew.replace("f", "Y")
        sNew = sNew.replace("l", "C")
        sNew = sNew.replace("w", "V")
        sNew = sNew.replace("j", ",")
        sNew = sNew.replace("m", "K")
        sNew = sNew.replace(";", "'")
        sNew = sNew.replace("d", "P")
        sNew = sNew.replace("h", "W")
        sNew = sNew.replace("n", "-")
        sNew = sNew.replace("u", "J")
        sNew = sNew.replace("y", '"')
        sNew = sNew.replace("i", "X")
        sNew = sNew.replace("o", "Z")
        sNew = sNew.replace("b", ".")

        print(sNew)

# with open("B:/Crypto4130/HW1/decrypt.txt", encoding = "utf-8", mode = 'w') as outfile:
#     outfile.write(sNew)
