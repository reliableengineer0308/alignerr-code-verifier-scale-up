from collections import deque
import sys

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [0] * n
        self.ptr = [0] * n
        
    def add_edge(self, u, v, cap):
        forward_idx = len(self.graph[u])
        backward_idx = len(self.graph[v])
        
        self.graph[u].append([v, cap, backward_idx])
        self.graph[v].append([u, 0, forward_idx])
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        
        while q:
            u = q.popleft()
            for edge in self.graph[u]:
                v, cap, rev_idx = edge
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        
        return self.level[t] != -1
    
    def dfs(self, u, t, f):
        if u == t:
            return f
            
        for i in range(self.ptr[u], len(self.graph[u])):
            self.ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            
            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, t, min(f, cap))
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed
        return 0
    
    def max_flow(self, s, t):
        max_flow = 0
        while self.bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                max_flow += pushed
        return max_flow
    
    def get_flows(self, original_edges):
        flows = []
        for u, v, original_cap in original_edges:
            flow_found = False
            for edge in self.graph[u]:
                if edge[0] == v:
                    residual_cap = edge[1]
                    flow = original_cap - residual_cap
                    flows.append(flow)
                    flow_found = True
                    break
            
            if not flow_found:
                flows.append(0)
        return flows

def solve_max_flow():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        try:
            N = int(input[idx]); M = int(input[idx+1]); idx += 2
            S = int(input[idx]); T = int(input[idx+1]); idx += 2
            if not (0 <= S < N and 0 <= T < N):
                raise ValueError(f"Source or sink out of range: S={S}, T={T}, N={N}")
            
            dinic = Dinic(N)
            original_edges = []
            
            for _ in range(M):
                u = int(input[idx]); v = int(input[idx+1]); c = int(input[idx+2]); idx += 3
                if not (0 <= u < N and 0 <= v < N):
                    raise ValueError(f"Invalid edge: {u}->{v}")
                if c < 0:
                    raise ValueError(f"Negative capacity: {c}")
                
                dinic.add_edge(u, v, c)
                original_edges.append((u, v, c))
            
            max_flow = dinic.max_flow(S, T)
            flows = dinic.get_flows(original_edges)
            
            results.append(f"Case #{case_num}: {max_flow}")
            results.append(" ".join(map(str, flows)))
            
        except Exception as e:
            results.append(f"Case #{case_num}: ERROR - {str(e)}")
            while idx < len(input) and not input[idx].isdigit():
                idx += 1
    
    return results