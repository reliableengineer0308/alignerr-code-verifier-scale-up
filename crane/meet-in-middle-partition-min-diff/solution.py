import bisect

def generate_subset_sums(arr):
    """Generate all possible subset sums for given array"""
    n = len(arr)
    sums = set()
    
    for mask in range(1 << n):
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):
                current_sum += arr[i]
        sums.add(current_sum)
    
    return sorted(sums)

def min_partition_difference(nums):
    """Find minimum absolute difference between two subset sums"""
    n = len(nums)
    total_sum = sum(nums)
    
    if n == 0:
        return 0
    
    # Split array into two halves
    mid = n // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    
    # Generate all subset sums for both halves
    left_sums = generate_subset_sums(left_arr)
    right_sums = generate_subset_sums(right_arr)
    
    # Remove duplicates and sort
    left_sums = sorted(set(left_sums))
    right_sums = sorted(set(right_sums))
    
    target = total_sum // 2
    min_diff = float('inf')
    
    # For each sum in left half, find best matching sum in right half
    for left_sum in left_sums:
        remaining = target - left_sum
        
        # Find closest value in right_sums to remaining
        pos = bisect.bisect_left(right_sums, remaining)
        
        # Check found position and position-1
        for i in [pos, pos-1]:
            if 0 <= i < len(right_sums):
                right_sum = right_sums[i]
                subset1_sum = left_sum + right_sum
                subset2_sum = total_sum - subset1_sum
                diff = abs(subset1_sum - subset2_sum)
                
                if diff < min_diff:
                    min_diff = diff
    
    return min_diff

def solve_min_partition_diff():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input[idx])
        idx += 1
        
        nums = []
        for i in range(n):
            nums.append(int(input[idx]))
            idx += 1
        
        result = min_partition_difference(nums)
        results.append(f"Case #{case_num}: {result}")
    
    return results