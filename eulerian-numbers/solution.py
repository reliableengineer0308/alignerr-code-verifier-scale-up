class EulerianNumbers:
    def __init__(self, max_n):
        self.max_n = max_n
        self.eulerian_cache = {}
    
    def compute_eulerian(self, mod):
        """Compute Eulerian numbers up to max_n modulo mod"""
        if mod in self.eulerian_cache:
            return self.eulerian_cache[mod]
        
        # Initialize DP table with larger size to handle n=0
        A = [[0] * (self.max_n + 2) for _ in range(self.max_n + 2)]
        A[0][0] = 1  # Base case: A(0,0) = 1
        
        for i in range(1, self.max_n + 1):
            A[i][0] = 1
            for j in range(1, i):
                A[i][j] = ((j + 1) * A[i-1][j] + (i - j) * A[i-1][j-1]) % mod
        
        self.eulerian_cache[mod] = A
        return A
    
    def get_eulerian(self, n, k, mod):
        """Get A(n, k) % mod"""
        if k >= n and n > 0:  # For n > 0, k >= n is 0
            return 0
        if n == 0 and k == 0:  # Special case: A(0,0) = 1
            return 1
        if n > self.max_n:
            self.max_n = n
            self.eulerian_cache.clear()
        
        if mod not in self.eulerian_cache:
            self.compute_eulerian(mod)
        
        return self.eulerian_cache[mod][n][k]

def solve_eulerian_numbers():
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
    
    eulerian_calculator = EulerianNumbers(max_n)
    
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx + 1])
        m = int(input[idx + 2])
        idx += 3
        
        result = eulerian_calculator.get_eulerian(n, k, m)
        results.append(str(result))
    
    return results