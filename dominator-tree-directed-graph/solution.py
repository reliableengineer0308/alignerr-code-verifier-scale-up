import sys
sys.setrecursionlimit(300000)

class DominatorTree:
    def __init__(self, n, edges, start=0):
        self.n = n
        self.start = start
        self.adj = [[] for _ in range(n)]
        self.rev_adj = [[] for _ in range(n)]
        
        for u, v in edges:
            self.adj[u].append(v)
            self.rev_adj[v].append(u)
        
        # Arrays for Lengauer-Tarjan
        self.dfn = [-1] * n
        self.idom = [-1] * n
        self.sdom = list(range(n))
        self.parent = [-1] * n
        self.bucket = [[] for _ in range(n)]
        self.ancestor = [-1] * n
        self.label = list(range(n))
        self.id = [-1] * n
        self.rev = [-1] * n
        self.cnt = 0
        
    def dfs(self, u):
        self.dfn[u] = self.cnt
        self.id[self.cnt] = u
        self.rev[u] = self.cnt
        self.cnt += 1
        for v in self.adj[u]:
            if self.dfn[v] == -1:
                self.parent[v] = u
                self.dfs(v)
    
    def compress(self, v):
        if self.ancestor[self.ancestor[v]] != -1:
            self.compress(self.ancestor[v])
            if self.dfn[self.sdom[self.label[self.ancestor[v]]]] < self.dfn[self.sdom[self.label[v]]]:
                self.label[v] = self.label[self.ancestor[v]]
            self.ancestor[v] = self.ancestor[self.ancestor[v]]
    
    def eval(self, v):
        if self.ancestor[v] == -1:
            return v
        self.compress(v)
        return self.label[v]
    
    def build(self):
        # Step 1: DFS to get DFS tree and numbering
        self.dfs(self.start)
        
        # Initialize
        for i in range(self.n):
            self.ancestor[i] = -1
        
        # Process nodes in reverse DFS order
        for i in range(self.cnt - 1, 0, -1):
            w = self.id[i]
            
            # Step 2: Compute semidominators
            for v in self.rev_adj[w]:
                if self.dfn[v] != -1:
                    u = self.eval(v)
                    if self.dfn[self.sdom[u]] < self.dfn[self.sdom[w]]:
                        self.sdom[w] = self.sdom[u]
            
            self.bucket[self.sdom[w]].append(w)
            self.ancestor[w] = self.parent[w]
            
            # Process bucket for parent
            for v in self.bucket[self.parent[w]]:
                u = self.eval(v)
                if self.dfn[self.sdom[u]] < self.dfn[self.sdom[v]]:
                    self.idom[v] = u
                else:
                    self.idom[v] = self.sdom[v]
            self.bucket[self.parent[w]] = []
        
        # Step 3: Final immediate dominator calculation
        for i in range(1, self.cnt):
            w = self.id[i]
            if self.idom[w] != self.sdom[w]:
                self.idom[w] = self.idom[self.idom[w]]
        
        # Set dominator for start node
        self.idom[self.start] = self.start
        
        # Handle unreachable nodes
        for i in range(self.n):
            if self.dfn[i] == -1:
                self.idom[i] = -1
        
        return self.idom

def solve_dominator_tree():
    input_data = sys.stdin.read().split()
    if not input_data:
        return []
    
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input_data[idx]); m = int(input_data[idx+1]); idx += 2
        
        edges = []
        for _ in range(m):
            u = int(input_data[idx]); v = int(input_data[idx+1]); idx += 2
            edges.append((u, v))
        
        dominator = DominatorTree(n, edges, 0)
        idom = dominator.build()
        
        results.append(f"Case #{case_num}:")
        for i in range(n):
            results.append(str(idom[i]))
    
    return results