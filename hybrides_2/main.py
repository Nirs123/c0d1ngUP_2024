entry = [17410, 16384, 11488, 8192, 6146, 5120, 4609, 4133, 4100, 4096, 3072, 2064, 2048, 1552, 1024, 644, 576, 520, 512, 264, 258, 256, 128, 64, 40, 32, 16, 8, 4, 2, 1]
target = [1, 1, 0, 2, 2, 2, 0, 2, 1, 0, 0, 1, 1, 2, 0]

entries = []
for i in range(len(entry)):
    test = bin(entry[i])[2:]

    start = [eval(i) for i in list(test)]
    for i in range(len(target) - len(test)):
        start.insert(0,0)

    entries.append(start)

def add(f, s):
    tmp = []
    for i in range(len(f)):
        tmp.append(f[i]+s[i])
    return tmp

def check(to_check, target):
    good = True
    for i in range(len(target)):
        if to_check[i] < target[i]:
            good = False
    return good

res = []
for i in range(len(entries)):
    for j in range(len(entries)):
        for k in range(len(entries)):
            for x in range(len(entries)):
                for y in range(len(entries)):
                    if check(add(entries[i],add(entries[j],add(entries[k],add(entries[x],entries[y])))),target):
                        print(( int(''.join(str(v) for v in entries[i]),2),
                                int(''.join(str(v) for v in entries[j]),2),
                                int(''.join(str(v) for v in entries[k]),2),
                                int(''.join(str(v) for v in entries[x]),2),
                                int(''.join(str(v) for v in entries[y]),2)))
