class DivisorCalculator:
    def __init__(self, limit):
        self.limit = limit
        self.spf = list(range(limit + 1))
        self._sieve()
    
    def _sieve(self):
        for i in range(2, int(self.limit**0.5) + 1):
            if self.spf[i] == i:
                for j in range(i*i, self.limit + 1, i):
                    if self.spf[j] == j:
                        self.spf[j] = i
    
    def get_divisor_info(self, n):
        if n == 1:
            return 1, 1
        
        count = 1
        total_sum = 1
        temp = n
        
        while temp > 1:
            p = self.spf[temp]
            exponent = 0
            while temp % p == 0:
                temp //= p
                exponent += 1
            
            count *= (exponent + 1)
            total_sum *= (pow(p, exponent + 1) - 1) // (p - 1)
        
        return count, total_sum

def solve_divisor_problem():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    numbers = [int(input[i]) for i in range(1, 1 + t)]
    
    max_n = max(numbers) if numbers else 1
    calculator = DivisorCalculator(max_n)
    results = []
    
    for n in numbers:
        count, total_sum = calculator.get_divisor_info(n)
        results.append(f"{count} {total_sum}")
    
    return results