base = "NNNGNBNNCUNGRBV"

ok =[
    ['A','C','G','U'],
    ['A','C','G','U'],
    ['A','C','G','U'],
    ['G'],
    ['A','C','G','U'],
    ['C','G','U'],
    ['A','C','G','U'],
    ['A','C','G','U'],
    ['C'],
    ['U'],
    ['A','C','G','U'],
    ['G'],
    ['A','G'],
    ['C','G','U'],
    ['A','C','G']
]

ok2 = [
    ['A','C','G','U'],
    ['G'],
    ['G','U'],
    ['A','U'],
    ['A'],
    ['A','G']
]

with open("entry.txt") as f:
    c = 0
    for line in f:
        line = line.replace("\n","")

        isGood = True
        for i in range(len(line)):
            if line[i] not in ok[i]:
                isGood = False

        if isGood:
            c += 1

    print(c)