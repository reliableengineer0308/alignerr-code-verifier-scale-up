class MobiusFunction:
    def __init__(self, limit):
        self.limit = limit
        self.mobius = [1] * (limit + 1)
        self.is_prime = [True] * (limit + 1)
        self._sieve()
    
    def _sieve(self):
        self.is_prime[0] = self.is_prime[1] = False
        self.mobius[1] = 1
        
        for i in range(2, self.limit + 1):
            if self.is_prime[i]:
                self.mobius[i] = -1
                for j in range(2*i, self.limit + 1, i):
                    self.is_prime[j] = False
                    self.mobius[j] = -self.mobius[j] if j % (i*i) != 0 else 0
    
    def get_mobius(self, n):
        """Get μ(n)"""
        return self.mobius[n]

def solve_mobius_function():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    max_n = max(numbers) if numbers else 1
    mobius_calculator = MobiusFunction(max_n)
    results = []
    
    for n in numbers:
        result = mobius_calculator.get_mobius(n)
        results.append(str(result))
    
    return results