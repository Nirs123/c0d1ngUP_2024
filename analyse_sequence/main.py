entry = "GCRNKMDUHBVGNSMRNCWNKDMANNVVYVCYKCGKHSAAUNGUNNAMGRUUCNAGKWSKSKGHKRAGDNABCVUGCMARBKACNKNNDSURCYVDBNSA"

def process(myChar):
    if myChar in ['A','C','G','U']:
        return 1
    elif myChar in ['R','Y','K','M','S','W']:
        return 2
    elif myChar in ['B','D','H','V']:
        return 3
    elif myChar in ['N']:
        return 4
    
nb_seq = 1
for char in entry:
    nb_seq *= process(char)

print(str(nb_seq)[len(str(nb_seq)) - 5 :])