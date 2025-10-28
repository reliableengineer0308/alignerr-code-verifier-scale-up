def solve(data):
    lines = data.strip().split('\n')
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    
    def build_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    max_periodic_length = 0
    
    # Precompute LPS for the entire string
    lps = build_lps(arr)
    
    # Check each prefix length from 2 to n
    for L in range(2, n + 1):
        period = L - lps[L - 1]
        if L % period == 0 and period <= L / 2:
            max_periodic_length = L
    
    return str(max_periodic_length)