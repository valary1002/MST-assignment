def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    n, e = map(int, lines[0].split())
    edges = []
    adj = [[] for _ in range(n)]

    for line in lines[1:]:
        u, v, w = map(int, line.split())
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))
    return n, edges, adj
