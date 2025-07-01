import heapq

def prim(n, adj):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]: continue
        visited[u] = True
        total_weight += weight

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst.append((u, v, w))
    return mst,total_weight