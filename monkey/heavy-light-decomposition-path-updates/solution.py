import sys
sys.setrecursionlimit(300000)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        # Build tree
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
    
    def push(self, idx, l, r):
        if self.lazy[idx] != 0:
            self.tree[idx] += self.lazy[idx]
            if l != r:
                self.lazy[2*idx] += self.lazy[idx]
                self.lazy[2*idx+1] += self.lazy[idx]
            self.lazy[idx] = 0
    
    def update_range(self, l, r, val, idx=1, segL=0, segR=None):
        if segR is None:
            segR = self.size - 1
        self.push(idx, segL, segR)
        
        if r < segL or l > segR:
            return
        
        if l <= segL and segR <= r:
            self.lazy[idx] += val
            self.push(idx, segL, segR)
            return
        
        mid = (segL + segR) // 2
        self.update_range(l, r, val, 2*idx, segL, mid)
        self.update_range(l, r, val, 2*idx+1, mid+1, segR)
        self.tree[idx] = max(self.tree[2*idx], self.tree[2*idx+1])
    
    def query_range(self, l, r, idx=1, segL=0, segR=None):
        if segR is None:
            segR = self.size - 1
        self.push(idx, segL, segR)
        
        if r < segL or l > segR:
            return 0
        
        if l <= segL and segR <= r:
            return self.tree[idx]
        
        mid = (segL + segR) // 2
        left_val = self.query_range(l, r, 2*idx, segL, mid)
        right_val = self.query_range(l, r, 2*idx+1, mid+1, segR)
        return max(left_val, right_val)
    
    def point_update(self, pos, val):
        self.update_range(pos, pos, val - self.query_range(pos, pos))

class HLD:
    def __init__(self, n, edges, values):
        self.n = n
        self.edges = edges
        self.values = values
        self.adj = [[] for _ in range(n+1)]
        self.parent = [0] * (n+1)
        self.depth = [0] * (n+1)
        self.heavy = [-1] * (n+1)
        self.head = [0] * (n+1)
        self.pos = [0] * (n+1)
        self.cur_pos = 0
        
        # Build adjacency list
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        self.dfs(1, 0)
        self.decompose(1, 1)
        
        # Build segment tree
        arr = [0] * (n+1)
        for i in range(1, n+1):
            arr[self.pos[i]] = self.values[i-1]
        self.seg_tree = SegmentTree(arr)
    
    def dfs(self, u, p):
        self.parent[u] = p
        self.depth[u] = self.depth[p] + 1
        size = 1
        max_size = 0
        
        for v in self.adj[u]:
            if v != p:
                child_size = self.dfs(v, u)
                size += child_size
                if child_size > max_size:
                    max_size = child_size
                    self.heavy[u] = v
        return size
    
    def decompose(self, u, h):
        self.head[u] = h
        self.pos[u] = self.cur_pos
        self.cur_pos += 1
        
        if self.heavy[u] != -1:
            self.decompose(self.heavy[u], h)
        
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self.decompose(v, v)
    
    def query_path(self, u, v):
        res = 0
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            res = max(res, self.seg_tree.query_range(self.pos[self.head[u]], self.pos[u]))
            u = self.parent[self.head[u]]
        
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res = max(res, self.seg_tree.query_range(self.pos[u], self.pos[v]))
        return res
    
    def update_path(self, u, v, val):
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            self.seg_tree.update_range(self.pos[self.head[u]], self.pos[u], val)
            u = self.parent[self.head[u]]
        
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        self.seg_tree.update_range(self.pos[u], self.pos[v], val)
    
    def update_node(self, u, val):
        self.seg_tree.point_update(self.pos[u], val)

def process_hld_queries(input_data):
    lines = input_data.strip().split('\n')
    n = int(lines[0])
    
    edges = []
    for i in range(1, n):
        u, v = map(int, lines[i].split())
        edges.append((u, v))
    
    values = list(map(int, lines[n].split()))
    q = int(lines[n+1])
    
    hld = HLD(n, edges, values)
    results = []
    
    for i in range(n+2, n+2+q):
        parts = lines[i].split()
        if parts[0] == 'QUERY_PATH':
            u, v = int(parts[1]), int(parts[2])
            results.append(str(hld.query_path(u, v)))
        elif parts[0] == 'UPDATE':
            u, x = int(parts[1]), int(parts[2])
            hld.update_node(u, x)
        elif parts[0] == 'ADD_PATH':
            u, v, x = int(parts[1]), int(parts[2]), int(parts[3])
            hld.update_path(u, v, x)
    
    return results