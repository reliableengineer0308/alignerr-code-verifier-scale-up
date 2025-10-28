from collections import deque
import sys

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [0] * n
        self.ptr = [0] * n
    
    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])
    
    def bfs(self, s, t):
        for i in range(self.n):
            self.level[i] = -1
            self.ptr[i] = 0
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for edge in self.graph[u]:
                v, cap, rev = edge
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1
    
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.ptr[u], len(self.graph[u])):
            v, cap, rev = self.graph[u][i]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, t, min(f, cap))
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
            self.ptr[u] += 1
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                flow += pushed
        return flow

def solve(data):
    idx = 0
    n, m, r, c = data[idx], data[idx+1], data[idx+2], data[idx+3]
    idx += 4
    
    # Read restaurant information
    restaurants = []
    for i in range(r):
        loc_id = data[idx]
        drivers = data[idx+1]
        idx += 2
        restaurants.append((loc_id, drivers))
    
    # Read customer information  
    customers = []
    for i in range(c):
        loc_id = data[idx]
        demand = data[idx+1]
        idx += 2
        customers.append((loc_id, demand))
    
    # Build the flow network
    # Nodes: 0 to n-1 are location nodes
    # Super source: n, super sink: n+1
    total_nodes = n + 2
    source = n
    sink = n + 1
    
    flow_net = MaxFlow(total_nodes)
    
    # Connect super source to restaurants
    for loc_id, drivers in restaurants:
        flow_net.add_edge(source, loc_id, drivers)
    
    # Connect customers to super sink
    for loc_id, demand in customers:
        flow_net.add_edge(loc_id, sink, demand)
    
    # Add road capacities
    for i in range(m):
        u = data[idx]
        v = data[idx+1]
        cap = data[idx+2]
        idx += 3
        flow_net.add_edge(u, v, cap)
    
    return flow_net.max_flow(source, sink)