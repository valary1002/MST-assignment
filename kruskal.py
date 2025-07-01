class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

