depart = 41495568832266240
taille = 100
etapes = 182


depart_bin = bin(depart)[2:]

start = [eval(i) for i in list(depart_bin)]
for i in range(taille - len(depart_bin)):
    start.insert(0,0)


def process_new(f, s, t):
    if [f,s,t] == [1,1,1]:
        return 0
    elif [f,s,t] == [1,1,0]:
        return 1
    elif [f,s,t] == [1,0,1]:
        return 1
    elif [f,s,t] == [1,0,0]:
        return 0
    elif [f,s,t] == [0,1,1]:
        return 1
    elif [f,s,t] == [0,1,0]:
        return 1
    elif [f,s,t] == [0,0,1]:
        return 1
    elif [f,s,t] == [0,0,0]:
        return 0
    
for i in range(etapes):
    tmp = [0] * taille
    for k in range(len(start)):
        if k == 0:
            tmp[k] = process_new(start[-1],start[k],start[k+1])
        elif k == taille-1:
            tmp[k] = process_new(start[k-1],start[k],start[0])
        else:
            tmp[k] = process_new(start[k-1],start[k],start[k+1])
    start = tmp

result = ''.join(str(v) for v in start)
print(int(result,2))