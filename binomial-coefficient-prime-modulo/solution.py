class BinomialCoefficient:
    def __init__(self, max_n, mod):
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        self.precomputed = False
        self.max_n = max_n
    
    def precompute(self):
        """Precompute factorials and inverse factorials up to max_n"""
        if self.precomputed:
            return
        
        # Compute factorials
        for i in range(1, self.max_n + 1):
            self.fact[i] = (self.fact[i-1] * i) % self.mod
        
        # Compute inverse factorials using Fermat's Little Theorem
        self.inv_fact[self.max_n] = pow(self.fact[self.max_n], self.mod-2, self.mod)
        for i in range(self.max_n, 0, -1):
            self.inv_fact[i-1] = (self.inv_fact[i] * i) % self.mod
        
        self.precomputed = True
    
    def nCr(self, n, k):
        """Compute C(n, k) % mod"""
        if k < 0 or k > n:
            return 0
        if not self.precomputed:
            self.precompute()
        return (self.fact[n] * self.inv_fact[k] % self.mod) * self.inv_fact[n-k] % self.mod

def solve_binomial_coefficient():
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
        temp_idx += 3
    
    # Initialize with maximum possible mod (will be updated per test case)
    # We'll create a new precomputation for each unique mod
    mod_to_calculator = {}
    
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx + 1])
        m = int(input[idx + 2])
        idx += 3
        
        if m not in mod_to_calculator:
            mod_to_calculator[m] = BinomialCoefficient(max_n, m)
        
        calculator = mod_to_calculator[m]
        result = calculator.nCr(n, k)
        results.append(str(result))
    
    return results