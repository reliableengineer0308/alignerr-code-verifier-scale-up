import sys
import bisect

class PersistentSegmentTree:
    def __init__(self, values):
        self.n = len(values)
        self.sorted_vals = sorted(set(values))
        self.comp_map = {val: idx for idx, val in enumerate(self.sorted_vals)}
        self.comp_arr = [self.comp_map[val] for val in values]
        
        # Prepare events for building persistent segment tree
        events = []
        for i, val in enumerate(self.comp_arr):
            events.append((val, i))
        events.sort()
        
        self.roots = [None] * (len(self.sorted_vals) + 1)
        self.build_tree(events)
    
    class Node:
        __slots__ = ('left', 'right', 'count')
        def __init__(self, count=0, left=None, right=None):
            self.count = count
            self.left = left
            self.right = right
    
    def build_tree(self, events):
        # Build initial empty tree
        def build(l, r):
            if l == r:
                return self.Node(0)
            mid = (l + r) // 2
            left_child = build(l, mid)
            right_child = build(mid + 1, r)
            return self.Node(left_child.count + right_child.count, left_child, right_child)
        
        self.roots[0] = build(0, self.n - 1)
        
        # Build persistent versions
        ptr = 0
        for version in range(1, len(self.sorted_vals) + 1):
            current_root = self.roots[version - 1]
            
            while ptr < len(events) and events[ptr][0] == version - 1:
                pos = events[ptr][1]
                current_root = self.update(current_root, 0, self.n - 1, pos, 1)
                ptr += 1
            
            self.roots[version] = current_root
    
    def update(self, node, l, r, pos, val):
        if l == r:
            return self.Node(node.count + val)
        
        mid = (l + r) // 2
        if pos <= mid:
            new_left = self.update(node.left, l, mid, pos, val)
            return self.Node(new_left.count + node.right.count, new_left, node.right)
        else:
            new_right = self.update(node.right, mid + 1, r, pos, val)
            return self.Node(node.left.count + new_right.count, node.left, new_right)
    
    def query_count_less_equal(self, version, ql, qr):
        """Count elements <= version in range [ql, qr]"""
        if version < 0:
            return 0
        if version >= len(self.roots):
            version = len(self.roots) - 1
            
        return self._query(self.roots[version], 0, self.n - 1, ql, qr)
    
    def _query(self, node, l, r, ql, qr):
        if not node or ql > r or qr < l:
            return 0
            
        if ql <= l and r <= qr:
            return node.count
        
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += self._query(node.left, l, mid, ql, qr)
        if qr > mid:
            res += self._query(node.right, mid + 1, r, ql, qr)
        return res

class ParallelBinarySearch:
    def __init__(self, arr, queries):
        self.arr = arr
        self.queries = queries
        self.n = len(arr)
        self.m = len(queries)
        
    def solve(self):
        if self.n == 0 or self.m == 0:
            return []
            
        # Build persistent segment tree
        pst = PersistentSegmentTree(self.arr)
        
        results = []
        for L, R, K in self.queries:
            l, r = L - 1, R - 1  # Convert to 0-indexed
            
            # Binary search for the k-th smallest element
            low, high = 0, len(pst.sorted_vals) - 1
            result_idx = high
            
            while low <= high:
                mid = (low + high) // 2
                # Count elements <= sorted_vals[mid] in range [l, r]
                count = pst.query_count_less_equal(mid + 1, l, r)
                
                if count >= K:
                    result_idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            results.append(pst.sorted_vals[result_idx])
        
        return results

def process_parallel_binary_search(input_data):
    """Process input data and return results for Parallel Binary Search"""
    data = input_data.strip().split()
    if not data:
        return []
    
    idx = 0
    n = int(data[idx]); idx += 1
    arr = list(map(int, data[idx:idx + n])); idx += n
    m = int(data[idx]); idx += 1
    
    queries = []
    for i in range(m):
        L = int(data[idx]); R = int(data[idx + 1]); K = int(data[idx + 2])
        idx += 3
        queries.append((L, R, K))
    
    pbs = ParallelBinarySearch(arr, queries)
    return pbs.solve()