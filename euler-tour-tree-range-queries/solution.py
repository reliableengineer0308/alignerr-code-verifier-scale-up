import sys
sys.setrecursionlimit(300000)

class EulerTourTree:
    def __init__(self, n, values):
        self.n = n
        self.values = [0] + values  # 1-indexed
        self.graph = [[] for _ in range(n+1)]
        self.in_time = [0] * (n+1)
        self.out_time = [0] * (n+1)
        self.parent = [[0] * 20 for _ in range(n+1)]
        self.depth = [0] * (n+1)
        self.timer = 0
        self.euler = []
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, u, p):
        self.timer += 1
        self.in_time[u] = self.timer
        self.euler.append(u)
        
        self.parent[u][0] = p
        self.depth[u] = self.depth[p] + 1
        
        for i in range(1, 20):
            self.parent[u][i] = self.parent[self.parent[u][i-1]][i-1]
        
        for v in self.graph[u]:
            if v != p:
                self.dfs(v, u)
        
        self.timer += 1
        self.out_time[u] = self.timer
        self.euler.append(u)
    
    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Lift u to same depth as v
        for i in range(19, -1, -1):
            if self.depth[u] - (1 << i) >= self.depth[v]:
                u = self.parent[u][i]
        
        if u == v:
            return u
        
        # Lift both until they have same parent
        for i in range(19, -1, -1):
            if self.parent[u][i] != self.parent[v][i]:
                u = self.parent[u][i]
                v = self.parent[v][i]
        
        return self.parent[u][0]

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)
    
    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res
    
    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

def solve_euler_tour():
    input = sys.stdin.read().split()
    idx = 0
    
    n = int(input[idx]); q = int(input[idx+1]); idx += 2
    values = []
    for i in range(n):
        values.append(int(input[idx])); idx += 1
    
    tree = EulerTourTree(n, values)
    
    # Read edges
    for i in range(n-1):
        u = int(input[idx]); v = int(input[idx+1]); idx += 2
        tree.add_edge(u, v)
    
    # Build Euler Tour
    tree.dfs(1, 0)
    
    # Build Fenwick Tree for Euler Tour array
    fenw = FenwickTree(2*n)
    
    # Initialize Fenwick Tree with node values
    # Each node appears twice in Euler Tour
    for i in range(1, n+1):
        fenw.update(tree.in_time[i], tree.values[i])
        fenw.update(tree.out_time[i], -tree.values[i])  # Negative for out-time
    
    results = []
    
    for _ in range(q):
        op = input[idx]; idx += 1
        if op == "UPDATE":
            u = int(input[idx]); x = int(input[idx+1]); idx += 2
            # Update the value
            old_val = tree.values[u]
            delta = x - old_val
            tree.values[u] = x
            
            fenw.update(tree.in_time[u], delta)
            fenw.update(tree.out_time[u], -delta)
            
        else:  # QUERY
            u = int(input[idx]); v = int(input[idx+1]); idx += 2
            lca_node = tree.lca(u, v)
            
            # Path sum = sum from root to u + sum from root to v - 2*sum from root to lca + value[lca]
            sum_u = fenw.query(tree.in_time[u])
            sum_v = fenw.query(tree.in_time[v])
            sum_lca = fenw.query(tree.in_time[lca_node])
            
            path_sum = sum_u + sum_v - 2 * sum_lca + tree.values[lca_node]
            results.append(str(path_sum))
    
    return results