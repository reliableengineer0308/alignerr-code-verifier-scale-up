import math

class Line:
    def __init__(self, a, b, index):
        self.a = a  # slope
        self.b = b  # intercept
        self.index = index
    
    def evaluate(self, t):
        return self.a * t + self.b
    
    def __repr__(self):
        return f"f(t)={self.a}*t + {self.b}"

class KineticTournament:
    def __init__(self, lines):
        self.lines = lines
        self.n = len(lines)
    
    def update(self, index, a, b):
        """Update a line"""
        self.lines[index] = Line(a, b, index)
    
    def query_naive(self, t):
        """Naive O(n) query for small n"""
        if not self.lines:
            return 0.0
        
        max_val = -float('inf')
        for line in self.lines:
            val = line.evaluate(t)
            if val > max_val:
                max_val = val
        
        return max_val

def solve_kinetic_tournament():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # Read initial parameters
    n = int(input[idx]); q = int(input[idx+1]); idx += 2
    
    # Read initial lines
    lines = []
    for i in range(n):
        a = float(input[idx]); b = float(input[idx+1]); idx += 2
        lines.append(Line(a, b, i))
    
    # Create kinetic tournament
    kt = KineticTournament(lines)
    results = []
    
    # Process operations
    for _ in range(q):
        op_type = input[idx]; idx += 1
        if op_type == "QUERY":
            t = float(input[idx]); idx += 1
            max_val = kt.query_naive(t)
            results.append(f"{max_val:.2f}")
        elif op_type == "UPDATE":
            i = int(input[idx]); a = float(input[idx+1]); b = float(input[idx+2]); idx += 3
            kt.update(i, a, b)
    
    return results