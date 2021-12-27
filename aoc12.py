
def get_inputs(path):
    with open(path, 'r') as file:
        inputs = [line.strip().split("-") for line in file]
    edges = {}
    for key, val in inputs:
        if not key in edges.keys():
            edges[key] = [val]
        else:
            edges[key].append(val)
        if not val in edges.keys():
            edges[val] = [key]
        else:
            edges[val].append(key)

    return edges


def walk(edges):
    if edges[0] == 'end's


def get_a(edges):
    paths = []
    curr = 'start'
    end = 'end'
    path = [curr]
    while not end in path:
        neigh = edges[curr]
        for n in neigh:
            if not n in path:
                path.append(n)
                curr = n
                
    print(path)


if __name__ == "__main__":
    edges = get_inputs("inputs/day12")
    edges = get_inputs("test/test12")

    print("Edges:", edges)
    
    get_a(edges)

