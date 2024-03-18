def check_sequence_rare(seq):
    for i in range(len(seq)-3):
        tmp = [seq[i] for i in range(i,i+4)]
        done = list(dict.fromkeys(tmp))
        if len(tmp) != len(done):
            return False
    return True


res = []
for i in range(1,501):
    with open(f"radio_enregistrements/enreg{"{:03d}".format(i)}.txt") as f:
        r = 0
        for line in f:
            line = line.replace("\n","")

            if check_sequence_rare(line):
                r+=1
        
        if r < 172 or r > 235:
            res.append(i)

print(res)