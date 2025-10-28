from collections import deque
import sys

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [0] * n
        self.ptr = [0] * n
        
    def add_edge(self, u, v, cap):
        """Add directed edge from u to v with given capacity"""
        forward_idx = len(self.graph[u])
        backward_idx = len(self.graph[v])
        
        # Forward edge: [destination, capacity, reverse_edge_index]
        self.graph[u].append([v, cap, backward_idx])
        # Backward edge: [destination, capacity, reverse_edge_index]
        self.graph[v].append([u, 0, forward_idx])
    
    def bfs(self, s, t):
        """Build level graph using BFS"""
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
        """Find blocking flow using DFS"""
        if u == t:
            return f
            
        for i in range(self.ptr[u], len(self.graph[u])):
            self.ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            
            if cap > 0 and self.level[v] == self.level[u] + 1:
                pushed = self.dfs(v, t, min(f, cap))
                if pushed > 0:
                    self.graph[u][i][1] -= pushed  # Reduce forward capacity
                    self.graph[v][rev_idx][1] += pushed  # Increase backward capacity
                    return pushed
        return 0
    
    def max_flow(self, s, t):
        """Compute maximum flow from s to t"""
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
        """Get flow values for original edges in input order"""
        flows = []
        for u, v, original_cap in original_edges:
            flow_found = False
            # Look for the forward edge in the residual graph
            for edge in self.graph[u]:
                if edge[0] == v:
                    residual_cap = edge[1]
                    # Flow = original capacity - residual capacity
                    flow = original_cap - residual_cap
                    flows.append(flow)
                    flow_found = True
                    break
            
            # If edge not found (shouldn't happen with proper implementation)
            if not flow_found:
                flows.append(0)
        return flows

def solve_max_flow():
    """Main function to solve multiple test cases"""
    input = sys.stdin.read().split()
    if not input:
        return []
    
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        try:
            # Read graph parameters
            N = int(input[idx]); M = int(input[idx+1]); idx += 2
            S = int(input[idx]); T = int(input[idx+1]); idx += 2
            
            # Validate source and sink
            if not (0 <= S < N and 0 <= T < N):
                raise ValueError(f"Invalid source or sink: S={S}, T={T}, N={N}")
            
            dinic = Dinic(N)
            original_edges = []
            
            # Read edges
            for _ in range(M):
                u = int(input[idx]); v = int(input[idx+1]); c = int(input[idx+2]); idx += 3
                if not (0 <= u < N and 0 <= v < N):
                    raise ValueError(f"Invalid edge: {u}->{v}")
                if c < 0:
                    raise ValueError(f"Negative capacity: {c}")
                
                dinic.add_edge(u, v, c)
                original_edges.append((u, v, c))
            
            # Compute maximum flow
            max_flow = dinic.max_flow(S, T)
            flows = dinic.get_flows(original_edges)
            
            # Store results
            results.append(f"Case #{case_num}: {max_flow}")
            results.append(" ".join(map(str, flows)))
            
        except Exception as e:
            results.append(f"Case #{case_num}: ERROR - {str(e)}")
            # Skip to next test case
            while idx < len(input) and not input[idx].isdigit():
                idx += 1
    
    return results

# For direct execution
if __name__ == "__main__":
    results = solve_max_flow()
    for result in results:
        print(result)