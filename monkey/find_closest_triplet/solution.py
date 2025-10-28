def find_closest_triplet(arr, target):
    n = len(arr)
    if n < 3:
        return None, None

    # Sort to enable two-pointer technique
    sorted_arr = sorted((val, idx) for idx, val in enumerate(arr))
    values = [x[0] for x in sorted_arr]
    
    best_sum = float('inf')
    best_triplet = None

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = values[i] + values[left] + values[right]
            
            # Update best if closer to target
            if abs(current_sum - target) < abs(best_sum - target):
                best_sum = current_sum
                best_triplet = (values[i], values[left], values[right])

            
            if current_sum < target:
                left += 1  # Need larger sum
            elif current_sum > target:
                right -= 1  # Need smaller sum
            else:
                # Exact match found
                return (values[i], values[left], values[right]), current_sum


    return best_triplet, best_sum

