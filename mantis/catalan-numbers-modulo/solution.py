class CatalanNumbers:
    def __init__(self, max_n):
        self.max_n = max_n
        self.catalan_cache = {}  # Cache for different moduli
    
    def compute_catalan_dp(self, mod):
        """Compute Catalan numbers up to max_n modulo mod using DP formula"""
        if mod in self.catalan_cache:
            return self.catalan_cache[mod]
        
        catalan = [0] * (self.max_n + 1)
        catalan[0] = 1
        
        for i in range(1, self.max_n + 1):
            for j in range(i):
                catalan[i] = (catalan[i] + (catalan[j] * catalan[i - 1 - j]) % mod) % mod
        
        self.catalan_cache[mod] = catalan
        return catalan
    
    def get_catalan(self, n, mod):
        """Get n-th Catalan number modulo mod"""
        if n > self.max_n:
            # Extend computation if needed
            self.max_n = n
            self.catalan_cache.clear()
        
        if mod not in self.catalan_cache:
            self.compute_catalan_dp(mod)
        
        return self.catalan_cache[mod][n]

def solve_catalan_numbers():
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
    
    catalan_calculator = CatalanNumbers(max_n)
    
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        result = catalan_calculator.get_catalan(n, m)
        results.append(str(result))
    
    return results