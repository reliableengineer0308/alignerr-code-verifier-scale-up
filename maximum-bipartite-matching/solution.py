import sys
from collections import deque

class HopcroftKarp:
    def __init__(self, u_size, v_size):
        self.u_size = u_size
        self.v_size = v_size
        self.graph = [[] for _ in range(u_size + 1)]
        self.pair_u = [0] * (u_size + 1)
        self.pair_v = [0] * (v_size + 1)
        self.dist = [0] * (u_size + 1)
    
    def add_edge(self, u, v):
        """Add edge from u in U to v in V"""
        self.graph[u].append(v)
    
    def bfs(self):
        """BFS to build level graph"""
        queue = deque()
        
        for u in range(1, self.u_size + 1):
            if self.pair_u[u] == 0:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        self.dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[0]:
                for v in self.graph[u]:
                    u_next = self.pair_v[v]
                    if self.dist[u_next] == float('inf'):
                        self.dist[u_next] = self.dist[u] + 1
                        queue.append(u_next)
        
        return self.dist[0] != float('inf')
    
    def dfs(self, u):
        """DFS to find augmenting path"""
        if u != 0:
            for v in self.graph[u]:
                u_next = self.pair_v[v]
                if self.dist[u_next] == self.dist[u] + 1:
                    if self.dfs(u_next):
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True
            self.dist[u] = float('inf')
            return False
        return True
    
    def max_matching(self):
        """Find maximum bipartite matching"""
        self.pair_u = [0] * (self.u_size + 1)
        self.pair_v = [0] * (self.v_size + 1)
        self.dist = [0] * (self.u_size + 1)
        
        matching = 0
        
        while self.bfs():
            for u in range(1, self.u_size + 1):
                if self.pair_u[u] == 0 and self.dfs(u):
                    matching += 1
        
        return matching

def solve_bipartite_matching():
    """Main function to handle multiple test cases"""
    data = sys.stdin.read().split()
    if not data:
        return []
    
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        m = int(data[idx]); n = int(data[idx+1]); e = int(data[idx+2]); idx += 3
        
        hk = HopcroftKarp(m, n)
        
        for _ in range(e):
            u = int(data[idx]); v = int(data[idx+1]); idx += 2
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        results.append(str(matching))
    
    return results

# For direct execution
if __name__ == "__main__":
    results = solve_bipartite_matching()
    for result in results:
        print(result)