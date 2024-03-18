nb_nodes = 5
powers = [100, 105, 105, 90, 100]

goal_path = [100, 105, 90]

roads = {}

with open("entry_test.txt") as f:
    c = 0
    for line in f:
        line = line.replace("\n","")
        line = line.replace(" ","")
        line = line.split(":")[1]

        arrivals = line.split(",")
        arrivals = [int(i) for i in arrivals]

        roads[c] = arrivals

        c += 1


print(roads)
print(powers)

def recursive_method(path):
    if len(path) == len(powers):
        return path
    elif len(path) == 0:
        for starting_point in roads.keys():
            if powers[starting_point] == goal_path[len(path)]:
                path.append(starting_point)
                return recursive_method(path)
    else:
        c = 0
        for target in roads[path[-1]]:
            if powers[target] == goal_path[len(path)]:
                path.append(target)
                c += 1
                return recursive_method(path)
        if c == 0:
            print("here")
            path.pop()
            return None

print(recursive_method([]))