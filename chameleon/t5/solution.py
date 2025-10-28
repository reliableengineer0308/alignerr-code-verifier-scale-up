import sys
from collections import deque

class HopcroftKarp:
    def __init__(self, U, V):
        self.U = U  
        self.V = V 
        self.graph = [[] for _ in range(U)]  
        self.pair_U = [-1] * U  
        self.pair_V = [-1] * V  
        self.dist = [0] * (U + 1) 
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self):
        queue = deque()
        
        # Initialize distances for BFS
        for u in range(self.U):
            if self.pair_U[u] == -1:  # Free node in U
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        # Sentinel node for unmatched nodes in V
        self.dist[self.U] = float('inf')
        
        # BFS to find shortest augmenting paths
        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[self.U]:
                for v in self.graph[u]:
                    u_next = self.pair_V[v]
                    if u_next == -1:
                        u_next = self.U  # Use sentinel for unmatched nodes
                    if self.dist[u_next] == float('inf'):
                        self.dist[u_next] = self.dist[u] + 1
                        queue.append(u_next)
        
        return self.dist[self.U] != float('inf')
    
    def dfs(self, u):
        if u == self.U:  # Reached sentinel node
            return True
            
        for v in self.graph[u]:
            u_next = self.pair_V[v]
            if u_next == -1:
                u_next = self.U
            if self.dist[u_next] == self.dist[u] + 1:
                if self.dfs(u_next):
                    self.pair_V[v] = u
                    self.pair_U[u] = v
                    return True
        self.dist[u] = float('inf')
        return False
    
    def maximum_matching(self):
        # Reset matching
        self.pair_U = [-1] * self.U
        self.pair_V = [-1] * self.V
        
        matching = 0
        # Repeatedly find augmenting paths
        while self.bfs():
            for u in range(self.U):
                if self.pair_U[u] == -1:  # Free node
                    if self.dfs(u):
                        matching += 1
        return matching
    
    def get_matching_pairs(self):
        pairs = []
        for u in range(self.U):
            if self.pair_U[u] != -1:
                pairs.append((u, self.pair_U[u]))
        pairs.sort()  # Sort by left node index
        return pairs

def is_valid_matching(U, V, edges, matching_pairs):
    # Check if all pairs are valid edges
    edge_set = set(edges)
    left_used = set()
    right_used = set()
    
    for u, v in matching_pairs:
        # Check if edge exists
        if (u, v) not in edge_set:
            return False
        # Check if nodes are unique
        if u in left_used or v in right_used:
            return False
        left_used.add(u)
        right_used.add(v)
    
    # Check if it's maximum by comparing with Hopcroft-Karp result
    hk = HopcroftKarp(U, V)
    for u, v in edges:
        hk.add_edge(u, v)
    
    max_possible = hk.maximum_matching()
    return len(matching_pairs) == max_possible

def find_maximum_matching(U, V, edges):
    hk = HopcroftKarp(U, V)
    for u, v in edges:
        hk.add_edge(u, v)
    
    max_matching = hk.maximum_matching()
    pairs = hk.get_matching_pairs()
    return max_matching, pairs

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    # Read input parameters
    U = int(data[0])
    V = int(data[1])
    E = int(data[2])
    idx = 3
    
    # Read edges
    edges = []
    for _ in range(E):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
    
    # Find maximum matching
    max_matching, pairs = find_maximum_matching(U, V, edges)
    
    # Output results
    print(f"Maximum matching: {max_matching}")
    if pairs:
        pairs_str = ", ".join(f"({u},{v})" for u, v in pairs)
        print(f"Matching pairs: {pairs_str}")
    else:
        print("No matching pairs")
    
    return pairs

if __name__ == "__main__":
    main()