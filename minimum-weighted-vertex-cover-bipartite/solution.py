from collections import deque
import sys

class BipartiteVertexCover:
    def __init__(self, n_left, n_right):
        self.n_left = n_left
        self.n_right = n_right
        self.n = n_left + n_right + 2
        self.source = n_left + n_right
        self.sink = n_left + n_right + 1
        self.graph = [[] for _ in range(self.n)]
        self.left_weights = [0] * n_left
        self.right_weights = [0] * n_right
        self.edges = []
        
    def set_weights(self, left_weights, right_weights):
        self.left_weights = left_weights
        self.right_weights = right_weights
        
    def add_edge(self, u, v):
        self.edges.append((u, v))
        
    def build_flow_network(self):
        # Connect source to left vertices with left weights
        for i in range(self.n_left):
            self.add_flow_edge(self.source, i, self.left_weights[i])
            
        # Connect right vertices to sink with right weights
        for i in range(self.n_right):
            self.add_flow_edge(self.n_left + i, self.sink, self.right_weights[i])
            
        # Connect left to right with infinite capacity
        for u, v in self.edges:
            self.add_flow_edge(u, self.n_left + v, float('inf'))
            
    def add_flow_edge(self, u, v, cap):
        forward_idx = len(self.graph[u])
        backward_idx = len(self.graph[v])
        self.graph[u].append([v, cap, backward_idx])
        self.graph[v].append([u, 0, forward_idx])
        
    def bfs(self, level, s, t):
        queue = deque()
        level[:] = [-1] * len(level)
        level[s] = 0
        queue.append(s)
        
        while queue:
            u = queue.popleft()
            for edge in self.graph[u]:
                v, cap, rev_idx = edge
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
                    
        return level[t] != -1
    
    def dfs(self, u, t, flow, level, ptr):
        if u == t:
            return flow
            
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = self.dfs(v, t, min(flow, cap), level, ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed
        return 0
    
    def max_flow(self):
        level = [-1] * self.n
        ptr = [0] * self.n
        flow = 0
        
        while self.bfs(level, self.source, self.sink):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(self.source, self.sink, float('inf'), level, ptr)
                if pushed == 0:
                    break
                flow += pushed
                
        return flow
    
    def find_min_cover(self):
        self.build_flow_network()
        min_weight = self.max_flow()
        
        # Find reachable vertices from source in residual graph
        visited = [False] * self.n
        queue = deque([self.source])
        visited[self.source] = True
        
        while queue:
            u = queue.popleft()
            for edge in self.graph[u]:
                v, cap, rev_idx = edge
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    
        # Construct vertex cover using min-cut
        left_cover = []
        right_cover = []
        
        # Left vertices NOT reachable from source are in the cover
        for i in range(self.n_left):
            if not visited[i]:
                left_cover.append(i)
                
        # Right vertices reachable from source are in the cover
        for i in range(self.n_right):
            if visited[self.n_left + i]:
                right_cover.append(i)
                
        return min_weight, left_cover, right_cover

def solve_bipartite_vertex_cover():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return []
        
    t = int(input_data[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        try:
            # Read n, m
            n = int(input_data[idx]); m = int(input_data[idx+1]); idx += 2
            
            # Read left weights
            left_weights = []
            for _ in range(n):
                left_weights.append(int(input_data[idx])); idx += 1
                
            # Read right weights
            right_weights = []
            for _ in range(m):
                right_weights.append(int(input_data[idx])); idx += 1
                
            # Read edges
            edges = []
            while idx < len(input_data):
                u = int(input_data[idx]); v = int(input_data[idx+1]); idx += 2
                if u == -1 and v == -1:
                    break
                edges.append((u, v))
                
            # Solve
            solver = BipartiteVertexCover(n, m)
            solver.set_weights(left_weights, right_weights)
            for u, v in edges:
                solver.add_edge(u, v)
                
            min_weight, left_cover, right_cover = solver.find_min_cover()
            
            # Format output
            results.append(f"Case #{case_num}: {min_weight}")
            left_str = "L: " + ",".join(map(str, left_cover)) if left_cover else "L: "
            right_str = "R: " + ",".join(map(str, right_cover)) if right_cover else "R: "
            results.append(left_str + " " + right_str)
            
        except Exception as e:
            results.append(f"Case #{case_num}: ERROR - {str(e)}")
            
    return results