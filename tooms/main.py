tooms = [10, 12, 6, 9, 18.5, 22, 7, 4, 9, 10]

res = []
with open("entry.txt") as f:
    c = 1
    for line in f:
        line = line.replace("\n","")
        line = line.split(" - ")[1]
        line = line.replace(" ","")
        
        tmp = line.split(",")

        for i in range(len(tmp)):
            tmp[i] = float(tmp[i])

        diff = tooms[0] - tmp[0]

        good = True
        for i in range(1,len(tmp)):
            if (tooms[i] - tmp[i]) != diff:
                good = False

        if good:
            res.append(c)

        c+=1

    print(sum(res))