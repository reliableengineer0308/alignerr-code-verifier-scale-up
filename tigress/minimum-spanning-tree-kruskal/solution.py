import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
    
    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))
    
    def find_mst(self):
        # Sort edges by weight
        self.edges.sort()
        
        uf = UnionFind(self.V)
        mst_edges = []
        total_weight = 0
        
        for w, u, v in self.edges:
            if uf.union(u, v):
                mst_edges.append((u, v, w))
                total_weight += w
                if len(mst_edges) == self.V - 1:
                    break
        
        # Check if graph is connected
        if len(mst_edges) == self.V - 1:
            return total_weight
        else:
            return "Disconnected Graph"

def solve_mst():
    """Main function to handle multiple test cases"""
    data = sys.stdin.read().split()
    if not data:
        return []
    
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        V = int(data[idx]); E = int(data[idx+1]); idx += 2
        
        kruskal = KruskalMST(V)
        
        for _ in range(E):
            u = int(data[idx]); v = int(data[idx+1]); w = int(data[idx+2]); idx += 3
            kruskal.add_edge(u, v, w)
        
        result = kruskal.find_mst()
        results.append(str(result))
    
    return results