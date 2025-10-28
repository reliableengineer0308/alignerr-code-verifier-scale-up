class MultinomialCalculator:
    def __init__(self, max_n):
        self.max_n = max_n
    
    def get_multinomial(self, n, groups, mod):
        """
        Compute multinomial coefficient C(n; k1,k2,...,km) % mod
        Using iterative combination computation to avoid modular inverse issues
        """
        result = 1
        remaining = n
        
        for k in groups:
            # Compute C(remaining, k) using iterative method
            comb = 1
            # Use the property: C(n, k) = product_{i=1}^k (n - k + i) / i
            for i in range(1, k + 1):
                comb = comb * (remaining - k + i) // i
            result = (result * comb) % mod
            remaining -= k
        
        return result

def solve_multinomial():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    calculator = MultinomialCalculator(1000)
    
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        group_count = int(input[idx])
        idx += 1
        
        groups = list(map(int, input[idx:idx + group_count]))
        idx += group_count
        
        result = calculator.get_multinomial(n, groups, m)
        results.append(str(result))
    
    return results