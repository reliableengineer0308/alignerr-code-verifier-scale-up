def longest_alternating_subsequence(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Initialize length with first element
    length = 1
    # Track last direction: 0 = undefined, 1 = increasing, -1 = decreasing
    last_direction = 0
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:  # Increasing
            if last_direction != 1:  # Can add if last wasn't increasing
                length += 1
                last_direction = 1
        elif arr[i] < arr[i - 1]:  # Decreasing
            if last_direction != -1:  # Can add if last wasn't decreasing
                length += 1
                last_direction = -1
    
    return length
