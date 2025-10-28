def count_inversions(arr):
    """
    Counts the number of inversions in an array using modified merge sort.
    
    An inversion is a pair (i, j) where i < j and arr[i] > arr[j].
    
    Uses divide-and-conquer approach with merge-sort-based inversion counting.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[int]): Input array of integers
        
    Returns:
        int: Total number of inversions
    """
    if not arr or len(arr) <= 1:
        return 0

    def merge_and_count(left, right):
        """
        Merges two sorted arrays and counts split inversions.
        
        When an element from the right array is selected before remaining elements
        in the left array, each remaining left element forms an inversion with it.
        
        Args:
            left (List[int]): Left sorted subarray
            right (List[int]): Right sorted subarray
            
        Returns:
            Tuple[List[int], int]: (merged sorted array, inversion count)
        """
        i = j = 0
        merged = []
        inversions = 0

        # Merge while counting split inversions
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # All remaining elements in left are > right[j]
                inversions += len(left) - i
                j += 1

        # Append leftover elements (no new inversions)
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    def sort_and_count(subarr):
        """
        Recursively sorts subarray and counts inversions.
        
        Divides array into halves, counts inversions in each half,
        then counts split inversions during merge.
        
        Args:
            subarr (List[int]): Subarray to sort and count
            
        Returns:
            Tuple[List[int], int]: (sorted subarray, total inversion count)
        """
        if len(subarr) <= 1:
            return subarr, 0

        mid = len(subarr) // 2
        left_half, left_inv = sort_and_count(subarr[:mid])
        right_half, right_inv = sort_and_count(subarr[mid:])

        merged, split_inv = merge_and_count(left_half, right_half)
        total_inv = left_inv + right_inv + split_inv

        return merged, total_inv

    # Execute recursive counting and return only inversion count
    _, total_inversions = sort_and_count(arr)
    return total_inversions

#  Optional: Alternative iterative version using index tracking
# (Included for educational purposes; main function uses recursive approach)
def count_inversions_iterative(arr):
    """
    Iterative version using explicit stack to avoid recursion depth issues.
    Less readable but prevents stack overflow for very large arrays.
    """
    if not arr or len(arr) <= 1:
        return 0
    
    # Implementation would use explicit stack with (subarray, start, end) tuples
    # and iterative merge process — omitted for brevity as recursive version is clearer
    raise NotImplementedError("Iterative version not implemented in this release")
