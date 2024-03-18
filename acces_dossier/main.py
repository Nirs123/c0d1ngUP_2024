all_cases = []
all_agents = []
agents_and_cases = {}

with open("entry.txt") as f:
    for line in f:
        line = line.replace("\n","")
        line = line.split(" - ")[1]
        tmp = line.split(" : ")

        if tmp[1] not in all_cases:
            all_cases.append(tmp[1])
        if tmp[0] not in all_agents:
            all_agents.append(tmp[0])

        if tmp[0] not in agents_and_cases.keys():
            agents_and_cases[tmp[0]] = [tmp[1]]
        else:
            agents_and_cases[tmp[0]].append(tmp[1])

# print(agents_and_cases)
# print(len(all_cases))
# print(len(all_agents))

def get_best_agent_to_draft(known_cases, drafted):
    res = {}
    for agent in all_agents:
        if agent not in drafted:
            total_cases = known_cases + agents_and_cases[agent]
            total_new_cases = list(set(total_cases))
            res[agent] = len(total_new_cases)
        
    sorted_res = sorted(res.items(), key=lambda x:x[1])
    
    return sorted_res[-1][0]

all_drafts = []
for agent in all_agents:
    drafted = [agent]
    known_cases = [case for case in agents_and_cases[agent]]

    while len(known_cases) < len(all_cases):
        new_agent = get_best_agent_to_draft(known_cases, drafted)
        total_cases = known_cases + agents_and_cases[new_agent]
        known_cases = list(set(total_cases))
        drafted.append(new_agent)

    all_drafts.append(drafted)

all_drafts.sort(key = lambda x:len(x))

print(", ".join(all_drafts[0]))
print(", ".join(all_drafts[1]))
print(", ".join(all_drafts[2]))