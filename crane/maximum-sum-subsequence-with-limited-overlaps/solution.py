def maxSumSubsequence(nums, k):
    """
    Finds maximum sum subsequence with ≤k consecutive picks.
    Time: O(n), Space: O(k)
    
    Args:
        nums: List of integers (can be negative)
        k: Max allowed consecutive picks (1 ≤ k ≤ len(nums))
    
    Returns:
        Maximum sum of valid subsequence (0 if all negative and empty subseq is best)
    """
    if not nums:
        return 0

    # run[c] = max sum ending with exactly c consecutive picks (c from 0 to k)
    # Initialize with -inf to represent invalid states
    run = [float('-inf')] * (k + 1)
    run[0] = 0  # Base: empty subsequence has sum 0
    global_max = 0  # Track overall best sum


    for num in nums:
        # Create a copy of current run to avoid using updated values
        prev_run = run[:]

        # Update runs of length k down to 1 (reverse order to prevent overwriting)
        for c in range(k, 0, -1):
            if prev_run[c - 1] != float('-inf'):
                # Extend previous run of (c-1) consecutive picks with current num
                run[c] = prev_run[c - 1] + num
            else:
                run[c] = float('-inf')  # Can't extend


        # Reset run[0]: best sum if we skip current element
        # This is the max of all possible states from previous step
        run[0] = max(prev_run)


        # Update global best (ignore run[0] since it means "skip")
        current_best = max(run[1:])  # Max among runs with ≥1 consecutive pick
        if current_best != float('-inf'):
            global_max = max(global_max, current_best)


    return global_max
