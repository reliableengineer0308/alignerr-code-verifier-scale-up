import sys

class LazySegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        
        # Build the segment tree
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
    
    def push(self, idx, l, r):
        """Push lazy value to children"""
        if self.lazy[idx] != 0:
            # Apply the lazy value to current node
            self.tree[idx] += self.lazy[idx] * (r - l + 1)
            
            # Push to children if not leaf
            if l != r:
                self.lazy[2*idx] += self.lazy[idx]
                self.lazy[2*idx+1] += self.lazy[idx]
            
            # Reset lazy value
            self.lazy[idx] = 0
    
    def update_range(self, l, r, value, idx=1, segL=0, segR=None):
        """Update range [l, r] by adding value"""
        if segR is None:
            segR = self.size - 1
        
        # Push lazy value first
        self.push(idx, segL, segR)
        
        # No overlap
        if r < segL or l > segR:
            return
        
        # Complete overlap
        if l <= segL and segR <= r:
            self.lazy[idx] += value
            self.push(idx, segL, segR)
            return
        
        # Partial overlap
        mid = (segL + segR) // 2
        self.update_range(l, r, value, 2*idx, segL, mid)
        self.update_range(l, r, value, 2*idx+1, mid+1, segR)
        self.tree[idx] = self.tree[2*idx] + self.tree[2*idx+1]
    
    def query_range(self, l, r, idx=1, segL=0, segR=None):
        """Query sum in range [l, r]"""
        if segR is None:
            segR = self.size - 1
        
        # Push lazy value first
        self.push(idx, segL, segR)
        
        # No overlap
        if r < segL or l > segR:
            return 0
        
        # Complete overlap
        if l <= segL and segR <= r:
            return self.tree[idx]
        
        # Partial overlap
        mid = (segL + segR) // 2
        left_sum = self.query_range(l, r, 2*idx, segL, mid)
        right_sum = self.query_range(l, r, 2*idx+1, mid+1, segR)
        return left_sum + right_sum

def solve_segment_tree():
    """Main function to handle input and process queries"""
    data = sys.stdin.read().split()
    if not data:
        return []
    
    idx = 0
    n = int(data[idx]); q = int(data[idx+1]); idx += 2
    arr = list(map(int, data[idx:idx+n])); idx += n
    
    seg_tree = LazySegmentTree(arr)
    results = []
    
    for _ in range(q):
        op = data[idx]; idx += 1
        
        if op == "update":
            l = int(data[idx]); r = int(data[idx+1]); val = int(data[idx+2]); idx += 3
            seg_tree.update_range(l, r, val)
            
        elif op == "query":
            l = int(data[idx]); r = int(data[idx+1]); idx += 2
            result = seg_tree.query_range(l, r)
            results.append(str(result))
    
    return results