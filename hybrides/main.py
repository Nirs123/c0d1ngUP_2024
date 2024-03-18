okays = ['0001','1010','1100','0011']

res = []
with open("entry.txt") as f:
    c = 1
    for line in f:
        line = line.replace("\n","")
        line = line.split(":")[1]
        line = line.replace(" ","")
        tmp = [(line[i:i+4]) for i in range(0, len(line), 4)]
        
        good = True
        for quartet in tmp:
            if quartet not in okays:
                good = False

        if good == False:
            res.append(c)

        c += 1

print(res)