def find_peak_index(arr):
    """
    Find the index of peak element in mountain array using binary search
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            # Peak is to the right
            left = mid + 1
        else:
            # Peak is to the left or mid is peak
            right = mid
    
    return left

def solve_peak_element():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input[idx])
        idx += 1
        
        arr = []
        for i in range(n):
            arr.append(int(input[idx]))
            idx += 1
        
        peak_index = find_peak_index(arr)
        results.append(f"Case #{case_num}: {peak_index}")
    
    return results