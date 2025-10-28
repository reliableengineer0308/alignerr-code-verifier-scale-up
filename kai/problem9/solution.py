from collections import deque
import sys

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])
    
    def bfs(self, s, t, level):
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, rev in self.graph[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1
    
    def dfs(self, u, t, f, level, iter):
        if u == t:
            return f
        for i in range(iter[u], len(self.graph[u])):
            iter[u] = i
            v, cap, rev = self.graph[u][i]
            if cap > 0 and level[v] > level[u]:
                d = self.dfs(v, t, min(f, cap), level, iter)
                if d > 0:
                    self.graph[u][i][1] -= d
                    self.graph[v][rev][1] += d
                    return d
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        iter = [0] * self.n
        
        while self.bfs(s, t, level):
            for i in range(self.n):
                iter[i] = 0
            while True:
                f = self.dfs(s, t, float('inf'), level, iter)
                if f == 0:
                    break
                flow += f
        return flow

def solve(data):
    idx = 0
    n, m, k = data[idx], data[idx+1], data[idx+2]
    idx += 3
    
    safe_zones = data[idx:idx+k]
    idx += k
    
    people = []
    for i in range(n):
        people.append(data[idx])
        idx += 1
    
    # Create flow network
    # Nodes: 0 to n-1 are original buildings
    # Super source: n, super sink: n+1
    total_nodes = n + 2
    source = n
    sink = n + 1
    flow_network = MaxFlow(total_nodes)
    
    # Connect source buildings to super source
    total_people = 0
    for i in range(n):
        if people[i] > 0:
            flow_network.add_edge(source, i, people[i])
            total_people += people[i]
    
    # Connect safe zones to super sink with large capacity
    for safe in safe_zones:
        flow_network.add_edge(safe, sink, total_people * 10)  # Large enough
    
    # Add water routes (multiply capacity by 6 for 6 hours)
    for _ in range(m):
        u, v, cap = data[idx], data[idx+1], data[idx+2]
        idx += 3
        # Bidirectional routes in flood
        flow_network.add_edge(u, v, cap * 6)
        flow_network.add_edge(v, u, cap * 6)
    
    return flow_network.max_flow(source, sink)