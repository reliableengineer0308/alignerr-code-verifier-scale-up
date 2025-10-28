import sys
sys.setrecursionlimit(200000)

class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]
        self.rev_graph = [[] for _ in range(2 * n)]
        self.visited = [False] * (2 * n)
        self.order = []
        self.comp = [-1] * (2 * n)
    
    def add_clause(self, a, b):
        # Convert variable to node index: 
        # x_i: 2*i, ¬x_i: 2*i + 1
        def get_node(x):
            if x > 0:
                return 2 * (x - 1)
            else:
                return 2 * (-x - 1) + 1
        
        u = get_node(a)
        v = get_node(b)
        
        # Add implications: (¬a → b) and (¬b → a)
        self.graph[u ^ 1].append(v)  # ¬a → b
        self.graph[v ^ 1].append(u)  # ¬b → a
        
        self.rev_graph[v].append(u ^ 1)
        self.rev_graph[u].append(v ^ 1)
    
    def dfs1(self, u):
        self.visited[u] = True
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs1(v)
        self.order.append(u)
    
    def dfs2(self, u, cl):
        self.comp[u] = cl
        for v in self.rev_graph[u]:
            if self.comp[v] == -1:
                self.dfs2(v, cl)
    
    def is_satisfiable(self):
        # First DFS pass
        self.visited = [False] * (2 * self.n)
        self.order = []
        for i in range(2 * self.n):
            if not self.visited[i]:
                self.dfs1(i)
        
        # Second DFS pass on reversed graph
        self.comp = [-1] * (2 * self.n)
        cl = 0
        for u in reversed(self.order):
            if self.comp[u] == -1:
                self.dfs2(u, cl)
                cl += 1
        
        # Check for contradiction
        for i in range(self.n):
            if self.comp[2 * i] == self.comp[2 * i + 1]:
                return False, None
        
        # Build assignment
        assignment = [False] * self.n
        for i in range(self.n):
            # If comp[x] < comp[¬x], set x to True
            # Otherwise set x to False
            assignment[i] = self.comp[2 * i] < self.comp[2 * i + 1]
        
        return True, assignment

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0]); m = int(data[1])
    idx = 2
    
    two_sat = TwoSAT(n)
    
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        two_sat.add_clause(a, b)
    
    satisfiable, assignment = two_sat.is_satisfiable()
    
    if satisfiable:
        print("SATISFIABLE")
        # Print assignment as 1/0 for True/False
        assignment_str = " ".join("1" if val else "0" for val in assignment)
        print(assignment_str)
        return assignment
    else:
        print("UNSATISFIABLE")
        return []

if __name__ == "__main__":
    main()