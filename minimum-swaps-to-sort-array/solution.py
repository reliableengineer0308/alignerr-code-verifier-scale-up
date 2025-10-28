def minimum_swaps_to_sort(arr):
    """
    Find minimum number of swaps to sort an array of distinct integers.
    Uses cycle detection in permutation approach.
    
    Args:
        arr: List[int] - array of distinct integers
    
    Returns:
        int - minimum number of swaps required
    """
    if len(arr) <= 1:
        return 0

    n = len(arr)
    
    # Create sorted array and position map
    sorted_arr = sorted(arr)
    pos_map = {val: idx for idx, val in enumerate(sorted_arr)}
    
    visited = [False] * n
    total_swaps = 0

    for i in range(n):
        # If already visited or in correct position, skip
        if visited[i] or pos_map[arr[i]] == i:
            continue

        # Traverse the cycle
        cycle_length = 0
        j = i

        while not visited[j]:
            visited[j] = True
            # Where should current element be?
            target_pos = pos_map[arr[j]]
            j = target_pos
            cycle_length += 1

        # Each cycle of length k needs k-1 swaps
        total_swaps += cycle_length - 1

    return total_swaps
