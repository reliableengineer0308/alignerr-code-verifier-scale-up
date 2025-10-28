def solve(data):
    lines = data.strip().split('\n')
    n = int(lines[0])
    m = int(lines[1])
    text = list(map(int, lines[2].split()))
    pattern = list(map(int, lines[3].split()))
    
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
    
    def kmp_search(text, pattern):
        n = len(text)
        m = len(pattern)
        if m == 0 or n == 0:
            return 0
        
        lps = build_lps(pattern)
        count = 0
        i = 0  # index for text
        j = 0  # index for pattern
        
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == m:
                count += 1
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return count
    
    return str(kmp_search(text, pattern))