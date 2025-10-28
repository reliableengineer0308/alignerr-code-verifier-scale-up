def find_first_position(nums, target):
    """Find first occurrence of target using binary search"""
    left, right = 0, len(nums) - 1
    first_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            first_pos = mid
            right = mid - 1  # Continue searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return first_pos

def find_last_position(nums, target):
    """Find last occurrence of target using binary search"""
    left, right = 0, len(nums) - 1
    last_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            last_pos = mid
            left = mid + 1  # Continue searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return last_pos

def search_range(nums, target):
    """Find first and last position of target in sorted array"""
    first = find_first_position(nums, target)
    last = find_last_position(nums, target)
    return [first, last]

def solve_first_last_position():
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
        
        first, last = search_range(nums, target)
        results.append(f"Case #{case_num}: {first} {last}")
    
    return results

if __name__ == '__main__':
    results = solve_first_last_position()
    for result in results:
        print(result)