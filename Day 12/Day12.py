import collections


def read_map(file):
    with open(file, "r") as f:
        data = [[ord(j) for j in i.strip()] for i in f.readlines()]
        n, m = len(data), len(data[0])
        start = next(
            (i, data[i].index(ord("S"))) for i in range(n) if ord("S") in data[i]
        )
        end = next(
            (i, data[i].index(ord("E"))) for i in range(n) if ord("E") in data[i]
        )
        data[start[0]][start[1]] = ord("a")
        data[end[0]][end[1]] = ord("z")
        data = [
            [data[i][j] - ord("a") for j in range(m)] for i in range(n)
        ]  # subtract a
    return data, start, end, n, m


def make_graph(data, n, m):
    graph = {}
    for i in range(n):
        for j in range(m):
            graph[(i, j)] = set(
                c for c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]     #Down, up, left , right
                if 0 <= c[0] < n and 0 <= c[1] < m and data[c[0]][c[1]] - data[i][j] <= 1)
    return graph


def bfs(graph, start, end):
    if start == end:
        return [start]
    done = {start}
    queue = collections.deque([(start, [])])
    while queue:
        c, path = queue.popleft()
        done.add(c)
        for n in graph[c]:
            if n == end:
                return path + [c, n]
            if n in done:
                continue
            queue.append((n, path + [c]))
            done.add(n)
    return None


def part1(path):
    data, start, end, n, m = read_map(path)
    graph = make_graph(data, n, m)
    sol = bfs(graph, start, end)
    return len(sol) - 1


def part2(path):
    data, start, end, n, m = read_map(path)
    graph = make_graph(data, n, m)
    best = None
    for start in [g for g in graph if data[g[0]][g[1]] == 0]:
        sol = bfs(graph, start, end)
        if not sol:
            continue
        if not best or len(sol) < best:
            best = len(sol) - 1
        print(best)
    return best



print("PART 1")
print(part1("input.txt"))
print("PART 2")
print( part2("input.txt"))