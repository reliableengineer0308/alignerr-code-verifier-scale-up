import sys
from collections import deque

class MinCostMaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.parent = [-1] * n
        self.parent_edge = [-1] * n
        self.dist = [float('inf')] * n
        self.flow = 0
        self.cost = 0
    
    def add_edge(self, u, v, cap, cost):
        forward_idx = len(self.graph[u])
        backward_idx = len(self.graph[v])
        self.graph[u].append([v, cap, cost, backward_idx])
        self.graph[v].append([u, 0, -cost, forward_idx])
    
    def bellman_ford(self, s, t):
        self.dist = [float('inf')] * self.n
        self.dist[s] = 0
        self.parent = [-1] * self.n
        self.parent_edge = [-1] * self.n
        
        # Run Bellman-Ford
        for _ in range(self.n):
            updated = False
            for u in range(self.n):
                if self.dist[u] == float('inf'):
                    continue
                for idx, (v, cap, cost, rev_idx) in enumerate(self.graph[u]):
                    if cap > 0 and self.dist[v] > self.dist[u] + cost:
                        self.dist[v] = self.dist[u] + cost
                        self.parent[v] = u
                        self.parent_edge[v] = idx
                        updated = True
            if not updated:
                break
        
        # Check for negative cycles reachable from s and leading to t
        if self.dist[t] == float('inf'):
            return False
            
        return True
    
    def min_cost_max_flow(self, s, t):
        max_flow = 0
        min_cost = 0
        
        while self.bellman_ford(s, t):
            # Find minimum capacity on path
            flow_val = float('inf')
            cur = t
            while cur != s:
                u = self.parent[cur]
                idx = self.parent_edge[cur]
                cap = self.graph[u][idx][1]
                flow_val = min(flow_val, cap)
                cur = u
            
            # Update flow and cost
            max_flow += flow_val
            cur = t
            while cur != s:
                u = self.parent[cur]
                idx = self.parent_edge[cur]
                self.graph[u][idx][1] -= flow_val
                self.graph[cur][self.graph[u][idx][3]][1] += flow_val
                min_cost += flow_val * self.graph[u][idx][2]
                cur = u
        
        return max_flow, min_cost
    
    def get_flows(self, original_edges):
        flows = []
        for u, v, original_cap, original_cost in original_edges:
            flow_found = False
            for edge in self.graph[u]:
                if edge[0] == v and edge[2] == original_cost:
                    flow = original_cap - edge[1]
                    flows.append(flow)
                    flow_found = True
                    break
            if not flow_found:
                flows.append(0)
        return flows

def solve_min_cost_max_flow():
    input_data = sys.stdin.read().split()
    if not input_data:
        return []
    
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input_data[idx]); m = int(input_data[idx+1]); idx += 2
        s = int(input_data[idx]); t = int(input_data[idx+1]); idx += 2
        
        mcmf = MinCostMaxFlow(n)
        original_edges = []
        
        for _ in range(m):
            u = int(input_data[idx]); v = int(input_data[idx+1])
            cap = int(input_data[idx+2]); cost = int(input_data[idx+3])
            idx += 4
            
            mcmf.add_edge(u, v, cap, cost)
            original_edges.append((u, v, cap, cost))
        
        max_flow, min_cost = mcmf.min_cost_max_flow(s, t)
        flows = mcmf.get_flows(original_edges)
        
        results.append(f"Case #{case_num}: {max_flow} {min_cost}")
        results.append(" ".join(map(str, flows)))
    
    return results