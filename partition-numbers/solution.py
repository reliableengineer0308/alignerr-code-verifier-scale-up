class PartitionNumbers:
    def __init__(self, max_n):
        self.max_n = max_n
        self.partition_cache = {}
    
    def compute_partitions(self, mod):
        """Compute partition numbers up to max_n modulo mod using pentagonal number theorem"""
        if mod in self.partition_cache:
            return self.partition_cache[mod]
        
        p = [0] * (self.max_n + 1)
        p[0] = 1
        
        for n in range(1, self.max_n + 1):
            total = 0
            k = 1
            while True:
                # Generalized pentagonal numbers: k(3k-1)/2 and k(3k+1)/2
                pent1 = k * (3*k - 1) // 2
                pent2 = k * (3*k + 1) // 2
                
                if pent1 > n and pent2 > n:
                    break
                
                sign = 1 if k % 2 == 1 else -1
                
                if pent1 <= n:
                    total = (total + sign * p[n - pent1]) % mod
                if pent2 <= n:
                    total = (total + sign * p[n - pent2]) % mod
                
                k += 1
            
            p[n] = total % mod
        
        self.partition_cache[mod] = p
        return p
    
    def get_partition(self, n, mod):
        """Get p(n) % mod"""
        if n > self.max_n:
            self.max_n = n
            self.partition_cache.clear()
        
        if mod not in self.partition_cache:
            self.compute_partitions(mod)
        
        return self.partition_cache[mod][n]

def solve_partition_numbers():
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
    
    partition_calculator = PartitionNumbers(max_n)
    
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        result = partition_calculator.get_partition(n, m)
        results.append(str(result))
    
    return results