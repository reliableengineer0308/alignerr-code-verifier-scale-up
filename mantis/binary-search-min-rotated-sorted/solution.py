def find_min_rotated(nums):
    """
    Find minimum element in rotated sorted array using binary search
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    
    return nums[left]

def solve_min_rotated():
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
        
        result = find_min_rotated(nums)
        results.append(f"Case #{case_num}: {result}")
    
    return results