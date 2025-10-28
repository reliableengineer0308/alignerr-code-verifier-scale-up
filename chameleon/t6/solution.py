import sys
sys.setrecursionlimit(200000)

class KosarajuSCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev_graph = [[] for _ in range(n)]  # Transposed graph
        self.visited = [False] * n
        self.stack = []
        self.components = []
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.rev_graph[v].append(u)  # Add to transposed graph
    
    def first_dfs(self, u):
        self.visited[u] = True
        for v in self.graph[u]:  # Use original graph
            if not self.visited[v]:
                self.first_dfs(v)
        self.stack.append(u)
    
    def second_dfs(self, u, component):
        self.visited[u] = True
        component.append(u)
        for v in self.rev_graph[u]:  # Use TRANSPOSED graph here!
            if not self.visited[v]:
                self.second_dfs(v, component)
    
    def find_scc(self):
        # First DFS pass
        self.visited = [False] * self.n
        for i in range(self.n):
            if not self.visited[i]:
                self.first_dfs(i)
        
        # Second DFS pass on TRANSPOSED graph
        self.visited = [False] * self.n
        self.components = []
        
        while self.stack:
            u = self.stack.pop()
            if not self.visited[u]:
                component = []
                self.second_dfs(u, component)
                component.sort()
                self.components.append(component)
        
        self.components.sort(key=lambda x: x[0])
        return self.components

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    
    kosaraju = KosarajuSCC(n)
    
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        kosaraju.add_edge(u, v)
    
    components = kosaraju.find_scc()
    
    print(f"Number of SCCs: {len(components)}")
    for i, component in enumerate(components, 1):
        print(f"SCC {i}: {component}")
    
    return components

if __name__ == "__main__":
    main()