import sys

def build_suffix_array(s):
    """Build suffix array using simple sorting method"""
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [idx for _, idx in suffixes]

def build_lcp_array(s, suffix):
    """Build LCP array using Kasai's algorithm"""
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[suffix[i]] = i
    
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

def build_rmq(lcp):
    """Build RMQ table for LCP array"""
    n = len(lcp)
    if n == 0:
        return []
    
    k = (n).bit_length()
    st = [[0] * n for _ in range(k)]
    st[0] = lcp[:]
    
    for j in range(1, k):
        step = 1 << (j - 1)
        for i in range(n - (1 << j) + 1):
            st[j][i] = min(st[j-1][i], st[j-1][i + step])
    return st

def rmq_query(st, l, r):
    """Range Minimum Query on LCP array"""
    if l > r:
        return 0
    length = r - l + 1
    j = length.bit_length() - 1
    return min(st[j][l], st[j][r - (1 << j) + 1])

def find_kth_substring(s, suffix, lcp, k):
    """Find k-th lexicographically smallest distinct substring"""
    n = len(s)
    
    # 각 접미사에서 생성되는 새로운 고유 부분문자열 수 계산
    for i in range(n):
        # 이 접미사에서 생성할 수 있는 새로운 부분문자열 수
        # = (접미사 길이) - (이전 접미사와의 LCP)
        suffix_length = n - suffix[i]
        prev_lcp = lcp[i] if i > 0 else 0
        
        # 새로운 고유 부분문자열 수
        new_substrings = suffix_length - prev_lcp
        
        if k <= new_substrings:
            # k번째 부분문자열은 이 접미사에서 시작
            # 부분문자열: s[suffix[i]:suffix[i] + prev_lcp + 1] 부터
            #            s[suffix[i]:suffix[i] + prev_lcp + k] 까지
            start = suffix[i]
            end = suffix[i] + prev_lcp + k
            return s[start:end]
        else:
            k -= new_substrings
    
    return ""

def solve_suffix_array():
    input = sys.stdin.read().splitlines()
    if not input:
        return []
    
    s = input[0].strip()
    q = int(input[1])
    
    # Build suffix array and LCP
    suffix = build_suffix_array(s)
    lcp = build_lcp_array(s, suffix)
    
    # Build RMQ for efficient LCP queries
    rmq_table = build_rmq(lcp)
    
    n = len(s)
    results = []
    
    for i in range(2, 2 + q):
        query = input[i].split()
        if query[0] == "LCP":
            i_idx = int(query[1])
            j_idx = int(query[2])
            
            if i_idx == j_idx:
                # Same suffix: LCP is the entire suffix length
                results.append(str(n - suffix[i_idx]))
            else:
                # LCP between two suffixes is the minimum in range [min+1, max]
                if i_idx > j_idx:
                    i_idx, j_idx = j_idx, i_idx
                
                if i_idx + 1 <= j_idx:
                    lcp_val = rmq_query(rmq_table, i_idx + 1, j_idx)
                else:
                    lcp_val = 0
                results.append(str(lcp_val))
                
        else:  # KTH
            k_val = int(query[1])
            substring = find_kth_substring(s, suffix, lcp, k_val)
            results.append(substring)
    
    return results