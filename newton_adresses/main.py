from collections import OrderedDict
base = "1a1c1d4e1i1m1n2r3s1t1u"

def encrypt(base : str):
    dic = {}
    for char in base:
        if char not in [" ","-"]:
            if char in dic.keys():
                dic[char] += 1
            else:
                dic[char] = 1

    sorted_dict = OrderedDict(sorted(dic.items()))

    final = ""
    for key,value in sorted_dict.items():
        final += str(value)
        final += key

    return final

with open("entry.txt") as f:
    for line in f:
        line = line.replace("\n","")

        if encrypt(line) == base:
            print(line)