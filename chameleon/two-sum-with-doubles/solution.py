def two_sum_with_doubles(nums, target):
    """
    Finds all unique index pairs (i, j) such that nums[i] + nums[j] == target and i < j.
    
    Args:
        nums (List[int]): Input array of integers
        target (int): Target sum
    
    Returns:
        List[Tuple[int, int]]: List of (i, j) pairs with i < j and nums[i]+nums[j]==target
    """
    if not nums or len(nums) < 2:
        return []
    
    # Map each value to list of its indices
    index_map = {}
    for idx, num in enumerate(nums):
        if num not in index_map:
            index_map[num] = []
        index_map[num].append(idx)

    result = []

    # For each number, check if its complement exists
    for num in index_map:
        complement = target - num

        if complement not in index_map:
            continue

        # Case 1: num == complement (e.g., target=10, num=5)
        if num == complement:
            indices = index_map[num]
            # All pairs (i, j) where i < j within the same number's indices
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    result.append((indices[i], indices[j]))
        # Case 2: num != complement
        else:
            # Take all combinations where index of num < index of complement
            for i in index_map[num]:
                for j in index_map[complement]:
                    if i < j:
                        result.append((i, j))

    # Sort result for consistent output (optional)
    return sorted(result)
