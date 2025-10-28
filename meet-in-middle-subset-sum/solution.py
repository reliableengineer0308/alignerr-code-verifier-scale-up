import bisect

def generate_subset_sums(arr):
    """Generate all possible subset sums for given array"""
    n = len(arr)
    sums = set()
    
    # Use bitmask to generate all subsets
    for mask in range(1 << n):
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):
                current_sum += arr[i]
        sums.add(current_sum)
    
    return sorted(sums)

def closest_subset_sum(nums, target):
    """Find subset sum closest to target using meet-in-the-middle"""
    n = len(nums)
    
    if n == 0:
        return 0
    
    # Split array into two halves
    mid = n // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    
    # Generate all subset sums for both halves
    left_sums = generate_subset_sums(left_arr)
    right_sums = generate_subset_sums(right_arr)
    
    # Include empty subset
    left_sums.append(0)
    right_sums.append(0)
    
    # Remove duplicates and sort
    left_sums = sorted(set(left_sums))
    right_sums = sorted(set(right_sums))
    
    best_diff = float('inf')
    best_sum = float('inf')  # Initialize with large value to pick smaller sum when ties
    
    # For each sum in right half, find best matching sum in left half
    for right_sum in right_sums:
        remaining = target - right_sum
        
        # Find closest value in left_sums to remaining
        pos = bisect.bisect_left(left_sums, remaining)
        
        # Check found position and position-1
        for i in [pos, pos-1]:
            if 0 <= i < len(left_sums):
                left_sum = left_sums[i]
                total = left_sum + right_sum
                diff = abs(total - target)
                
                # If better difference, or same difference but smaller sum
                if diff < best_diff or (diff == best_diff and total < best_sum):
                    best_diff = diff
                    best_sum = total
    
    return best_sum

def solve_meet_in_middle():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input[idx])
        target = int(input[idx + 1])
        idx += 2
        
        nums = []
        for i in range(n):
            nums.append(int(input[idx]))
            idx += 1
        
        result = closest_subset_sum(nums, target)
        results.append(f"Case #{case_num}: {result}")
    
    return results