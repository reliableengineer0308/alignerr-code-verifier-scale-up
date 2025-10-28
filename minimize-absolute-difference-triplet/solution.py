def minimize_abs_diff_triplet(arr):
    n = len(arr)
    
    if n < 3:
        return None, None
    
    # Key insight: |a−b| + |b−c| + |c−a| = 2 × (max(a,b,c) − min(a,b,c))
    # So we need to minimize (max - min) among triplets
    # Best candidates are consecutive elements in sorted array
    
    sorted_arr = sorted(arr)
    min_diff = float('inf')
    best_triplet = None

    # Check all consecutive triplets in sorted array
    for i in range(n - 2):
        a, b, c = sorted_arr[i], sorted_arr[i + 1], sorted_arr[i + 2]
        current_diff = 2 * (c - a)  # Since c ≥ b ≥ a
        
        if current_diff < min_diff:
            min_diff = current_diff
            best_triplet = (a, b, c)

    return best_triplet, float(min_diff)
