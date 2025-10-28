def max_subarray_sum_constrained(arr, min_len, max_len):
    n = len(arr)
    
    # Edge case: empty array or impossible constraints
    if n == 0 or min_len > n:
        return 0
    
    # Ensure max_len doesn't exceed array length
    max_len = min(max_len, n)
    
    # Precompute prefix sums for O(1) range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    max_sum = float('-inf')

    # For each possible ending position
    for end in range(min_len - 1, n):
        # Check all valid lengths from min_len to max_len (or until start=0)
        for length in range(min_len, min(max_len + 1, end + 2)):
            start = end - length + 1
            if start < 0:
                continue
            current_sum = prefix[end + 1] - prefix[start]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum if max_sum != float('-inf') else 0
