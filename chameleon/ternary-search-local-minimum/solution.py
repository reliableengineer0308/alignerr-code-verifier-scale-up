def find_local_minimum(arr):
    """
    Find a local minimum in array using modified binary search
    """
    n = len(arr)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is local minimum
        left_neighbor = arr[mid - 1] if mid > 0 else float('inf')
        right_neighbor = arr[mid + 1] if mid < n - 1 else float('inf')
        
        if arr[mid] < left_neighbor and arr[mid] < right_neighbor:
            return arr[mid]
        
        # If left neighbor is smaller, search left half
        if mid > 0 and arr[mid - 1] < arr[mid]:
            right = mid - 1
        # If right neighbor is smaller, search right half  
        else:
            left = mid + 1
    
    return arr[left] if left < n else arr[0]

def solve_local_minimum():
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
        
        result = find_local_minimum(arr)
        results.append(f"Case #{case_num}: {result}")
    
    return results