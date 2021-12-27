from queue import PriorityQueue

def get_inputs(path):
    with open(path, 'r') as file:
        cave_map = [list(map(int, list(line.strip()))) for line in file]
    return cave_map


def mult_row(row):
    tmp = []
    for i in range(5):
        tmp += [c + i if (c + i) < 10 else ((c + i) % 10) + 1 for c in row]
    return tmp


def mult_col(row, i):
    return [c + i if (c + i) < 10 else ((c + i) % 10) + 1 for c in row]


def mult_map(cave_map):
    rows = []
    for row in cave_map:
        rows.append(mult_row(row))

    res = []
    for i in range(5):
        for row in rows:
            res.append(mult_col(row, i))
    
    return res


def make_graph(cave_map):
    cave_graph = {}
    # visited = {}
    for y in range(len(cave_map)):
        for x in range(len(cave_map[0])):
            cave_graph[(x, y)] = cave_map[y][x]
            # visited[(x, y)] = False
    return cave_graph # , visited


def dijkstra(cave_graph, start, end):
    dist = {(start, end): 0}
    prev = {}
    pq = PriorityQueue()
    move_x = [0, 0, -1, 1]
    move_y = [-1, 1, 0, 0]

    for v in cave_graph:
        if not (start, end) == v:
            dist[v] = float('inf')    
            prev[v] = None
        pq.put(v, dist[v])

    while not pq.empty():
        u = pq.get()
        for i in range(4):
            x = u[0] + move_x[i]
            y = u[1] + move_y[i]
            v = (x, y)
            if v in cave_graph:
                alt = dist[u] + cave_graph[v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    pq.put(v, alt)

    return dist, prev


if __name__ == "__main__":
    cave_map = get_inputs("inputs/day15")
    # cave_map = get_inputs("test/test15")


    cave_graph = make_graph(cave_map)

    dist, prev = dijkstra(cave_graph, 0, 0)

    print(dist[(len(cave_map[0]) - 1, len(cave_map) - 1)])

    mult_cave = mult_map(cave_map)

    cave_graph = make_graph(mult_cave)

    dist, prev = dijkstra(cave_graph, 0, 0)

    print(dist[(len(mult_cave[0]) - 1, len(mult_cave) - 1)])
