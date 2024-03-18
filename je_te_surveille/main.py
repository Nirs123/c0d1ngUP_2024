import math
plan = {}
all_agents = [] 
with open("entry.txt") as f:
    c = 0
    for line in f:
        line = line.replace("\n","")
        line = line.replace(" ","")
        tmp = line.split(",")
        plan[c] = [int(tmp[0]),int(tmp[1])]
        all_agents.append(c)

        c += 1

targets = {}
for agent,pos in plan.items():
    res_tmp = {}
    for targ,pos_target in plan.items():
        if agent != targ:
            res_tmp[targ] = math.dist(pos,pos_target)
    
    targets[agent] = min(res_tmp, key=res_tmp.get)
    
for target in targets.values():
    if target in all_agents:
        all_agents.remove(target)

print(all_agents)