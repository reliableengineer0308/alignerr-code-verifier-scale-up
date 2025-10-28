class Derangements:
    def __init__(self, max_n):
        self.max_n = max_n
        self.derangements = None
    
    def compute_derangements(self, mod):
        """Compute derangements up to max_n modulo mod"""
        if self.derangements is not None and len(self.derangements) > self.max_n:
            return
        
        derangements = [0] * (self.max_n + 1)
        derangements[0] = 1  # !0 = 1
        
        if self.max_n >= 1:
            derangements[1] = 0  # !1 = 0
        
        for i in range(2, self.max_n + 1):
            derangements[i] = ((i - 1) * (derangements[i - 1] + derangements[i - 2])) % mod
        
        self.derangements = derangements
    
    def get_derangement(self, n, mod):
        """Get !n % mod"""
        if self.derangements is None or len(self.derangements) <= n:
            self.compute_derangements(mod)
        return self.derangements[n]

def solve_derangements():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    # Find maximum n for precomputation
    max_n = 0
    temp_idx = idx
    for _ in range(t):
        n = int(input[temp_idx])
        max_n = max(max_n, n)
        temp_idx += 2
    
    derangement_calculator = Derangements(max_n)
    
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        result = derangement_calculator.get_derangement(n, m)
        results.append(str(result))
    
    return results