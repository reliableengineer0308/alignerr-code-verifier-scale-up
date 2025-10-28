import heapq

class MedianMaintainer:
    def __init__(self):
        self.max_heap = []  # Lower half (use negative values for max-heap)
        self.min_heap = []  # Upper half
    
    
    def add_number(self, num):
        """Add a number to the stream and maintain heaps."""
        # Add to appropriate heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance heaps
        self._balance_heaps()
    
    
    def _balance_heaps(self):
        """Ensure size difference ≤ 1."""
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            # Move from min_heap to max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    
    def get_median(self):
        """Return current median."""
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) // 2
        else:
            return -self.max_heap[0]  # max_heap has extra element

def median_maintenance(stream):
    """
    Compute medians for a stream of numbers.
    
    Args:
        stream (List[int]): Sequence of incoming numbers
    
    Returns:
        List[int]: Medians after each insertion
    """
    if not stream:
        return []
    
    median_tracker = MedianMaintainer()
    result = []
    
    for num in stream:
        median_tracker.add_number(num)
        result.append(median_tracker.get_median())
    
    
    return result
