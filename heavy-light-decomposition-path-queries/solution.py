import sys
sys.setrecursionlimit(300000)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [-10**18] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
    
    def update(self, index, value):
        pos = self.size + index
        self.tree[pos] = value
        pos //= 2
        while pos:
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos+1])
            pos //= 2
    
    def query(self, l, r):
        l += self.size
        r += self.size
        res = -10**18
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

class HLD:
    def __init__(self, n, values, edges):
        self.n = n
        self.values = values
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        # HLD arrays
        self.parent = [-1] * n
        self.depth = [0] * n
        self.heavy = [-1] * n
        self.head = [0] * n
        self.pos = [0] * n
        self.cur_pos = 0
        
        # First DFS: compute parent, depth, heavy children
        self.dfs1(0)
        
        # Second DFS: decompose chains
        self.dfs2(0, 0)
        
        # Build segment tree
        self.arr = [0] * n
        for i in range(n):
            self.arr[self.pos[i]] = self.values[i]
        self.seg_tree = SegmentTree(self.arr)
    
    def dfs1(self, v):
        size = 1
        max_size = 0
        for u in self.adj[v]:
            if u != self.parent[v]:
                self.parent[u] = v
                self.depth[u] = self.depth[v] + 1
                child_size = self.dfs1(u)
                size += child_size
                if child_size > max_size:
                    max_size = child_size
                    self.heavy[v] = u
        return size
    
    def dfs2(self, v, h):
        self.head[v] = h
        self.pos[v] = self.cur_pos
        self.cur_pos += 1
        if self.heavy[v] != -1:
            self.dfs2(self.heavy[v], h)
        for u in self.adj[v]:
            if u != self.parent[v] and u != self.heavy[v]:
                self.dfs2(u, u)
    
    def update_node(self, node, value):
        self.seg_tree.update(self.pos[node], value)
    
    def query_path(self, u, v):
        res = -10**18
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            res = max(res, self.seg_tree.query(self.pos[self.head[u]], self.pos[u]))
            u = self.parent[self.head[u]]
        
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res = max(res, self.seg_tree.query(self.pos[u], self.pos[v]))
        return res

def process_queries(n, values, edges, queries):
    hld = HLD(n, values, edges)
    results = []
    for query in queries:
        if query[0] == "UPDATE":
            node, new_value = query[1], query[2]
            hld.update_node(node, new_value)
        else:  # "QUERY"
            u, v = query[1], query[2]
            results.append(hld.query_path(u, v))
    return results