from random import randint, shuffle


def check_connection(network, f, s):
    graph = {}
    for con in network:
        n1, n2 = con.split('-')
        graph[n1] = graph.get(n1, ()) + (n2,)
        graph[n2] = graph.get(n2, ()) + (n1,)
    neighbours = set(graph[f])
    visited = set()
    while neighbours:
        current = neighbours.pop()
        # if current in visited:
        #     continue
        visited.add(current)
        if current == s:
            return True
        for n in graph[current]:
            if n in visited:
                continue
            neighbours.add(n)
    return False

DRONE_NAMES = [
    "dr101",
    "mr99",
    "out00",
    "scout1",
    "scout2",
    "scout3",
    "scout4",
    "sscout",
    "super",
    "base",
    "mega",
    "nic",
    "doc",
    "plane1",
    "plane2",
    "nikola",
    "stevan",
    "sobhia",
    "night",
    "batman",
    "nwing",
    "robin",
    "cat",
    "pingin"

]


ans = check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
                 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
                "mr99", "scout3")

def gen_network(names=None, numb_names=None, numb_connections=None):
    numb_names = numb_names or randint(3, 10)
    if not names:
        shuffle(DRONE_NAMES)
        names = DRONE_NAMES[:numb_names]
    max_connections = sum(range(numb_names))
    numb_connections = min(numb_connections, max_connections) if numb_connections else randint(1, max_connections)
    all_connections = []
    for i, n1 in enumerate(names):
        for n2 in names[i+1:]:
            all_connections.append("{}-{}".format(n1, n2) if randint(0, 1) else "{}-{}".format(n2, n1))
    used_names = set()
    shuffle(all_connections)
    connections = all_connections[:numb_connections]
    for c in connections:
        n1, n2 = c.split("-")
        used_names.add(n1)
        used_names.add(n2)
    used_names = list(used_names)
    shuffle(used_names)
    return connections, used_names

net, names = gen_network(None, 2, 1)

def print_test(network, names, only_false=False):
    ans = check_connection(network, names[0], names[1])
    if not only_false or not ans:
        print('{{"input": ({},\n    "{}", "{}"),\n"answer": {},\n"explanation": {}\n}},'.format(network, names[0], names[1], ans, names))

# print_test(*gen_network(None, 2, 1))
# print_test(*gen_network(None, 4, 2))
# print_test(*gen_network(None, 10, 45))
# print_test(*gen_network(None, 10, 9))

for _ in range(20):
    print_test(*gen_network(), only_false=True)