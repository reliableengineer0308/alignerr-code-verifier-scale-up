import heapq
from collections import Counter

def top_k_frequent(nums, k):
    """
    Returns k most frequent elements in nums.
    
    Time: O(n + k log n)
    Space: O(n)
    """
    if not nums or k == 0:
        return []
    
    # Count frequencies - O(n)
    freq_map = Counter(nums)
    
    # Use heap to get top k frequent - O(k log n)
    # heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
    heap = [(-freq, num) for num, freq in freq_map.items()]
    heapq.heapify(heap)
    
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    
    
    return result
