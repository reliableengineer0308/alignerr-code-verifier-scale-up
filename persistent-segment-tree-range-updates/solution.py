import sys
sys.setrecursionlimit(300000)

class PersistentSegmentTree:
    class Node:
        __slots__ = ['left', 'right', 'sum', 'lazy']
        def __init__(self, left=None, right=None, sum_val=0, lazy=0):
            self.left = left
            self.right = right
            self.sum = sum_val
            self.lazy = lazy
    
    def __init__(self, n, arr):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.roots = []  # Store all version roots
        self.current_version = 0
        
        # Build initial tree (Version 0)
        def build(l, r):
            if l == r:
                return self.Node(sum_val=arr[l] if l < n else 0)
            mid = (l + r) // 2
            left_child = build(l, mid)
            right_child = build(mid + 1, r)
            return self.Node(left_child, right_child, left_child.sum + right_child.sum)
        
        self.roots.append(build(0, self.size - 1))
    
    def _copy_node(self, node):
        """Create a copy of a node"""
        if node is None:
            return None
        return self.Node(node.left, node.right, node.sum, node.lazy)
    
    def _apply(self, node, l, r, val):
        """Apply lazy value to node"""
        if node is None:
            return node
        new_node = self._copy_node(node)
        new_node.sum += val * (r - l + 1)
        new_node.lazy += val
        return new_node
    
    def _push(self, node, l, r):
        """Push lazy value to children"""
        if node.lazy != 0:
            mid = (l + r) // 2
            node.left = self._apply(node.left, l, mid, node.lazy)
            node.right = self._apply(node.right, mid + 1, r, node.lazy)
            node.lazy = 0
        return node
    
    def update(self, l, r, val):
        """Update range [l, r] with value val and create new version"""
        def _update(node, seg_l, seg_r, l, r, val):
            if r < seg_l or l > seg_r:
                return node
            
            if l <= seg_l and seg_r <= r:
                return self._apply(node, seg_l, seg_r, val)
            
            node = self._push(node, seg_l, seg_r)
            mid = (seg_l + seg_r) // 2
            
            left_child = _update(node.left, seg_l, mid, l, r, val)
            right_child = _update(node.right, mid + 1, seg_r, l, r, val)
            
            return self.Node(left_child, right_child, left_child.sum + right_child.sum)
        
        # Create new version
        new_root = _update(self.roots[self.current_version], 0, self.size - 1, l, r, val)
        self.roots.append(new_root)
        self.current_version = len(self.roots) - 1
        return self.current_version
    
    def query(self, l, r):
        """Query sum in range [l, r] in current version"""
        def _query(node, seg_l, seg_r, l, r):
            if node is None or r < seg_l or l > seg_r:
                return 0
            
            if l <= seg_l and seg_r <= r:
                return node.sum
            
            node = self._push(node, seg_l, seg_r)
            mid = (seg_l + seg_r) // 2
            
            left_sum = _query(node.left, seg_l, mid, l, r)
            right_sum = _query(node.right, mid + 1, seg_r, l, r)
            
            return left_sum + right_sum
        
        return _query(self.roots[self.current_version], 0, self.size - 1, l, r)
    
    def checkpoint(self):
        """Mark current version (no new version created)"""
        # Just return current version number
        return self.current_version
    
    def rollback(self, version):
        """Revert to specified version (no new version created)"""
        if version < 0 or version >= len(self.roots):
            raise ValueError(f"Invalid version: {version}")
        self.current_version = version
        return self.current_version

def solve_persistent_segment_tree(input_data):
    """
    Solve the persistent segment tree problem.
    
    Args:
        input_data: string containing input data
        
    Returns:
        string containing output data
    """
    data = input_data.split()
    if not data:
        return ""
    
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(data[idx]); q = int(data[idx+1]); idx += 2
        
        arr = []
        for _ in range(n):
            arr.append(int(data[idx])); idx += 1
        
        pst = PersistentSegmentTree(n, arr)
        
        case_results = [f"Case #{case_num}:"]
        
        for _ in range(q):
            op = data[idx]; idx += 1
            
            if op == "UPDATE":
                l = int(data[idx]); r = int(data[idx+1]); x = int(data[idx+2]); idx += 3
                pst.update(l, r, x)
                
            elif op == "QUERY":
                l = int(data[idx]); r = int(data[idx+1]); idx += 2
                result = pst.query(l, r)
                case_results.append(str(result))
                
            elif op == "CHECKPOINT":
                pst.checkpoint()
                # No operation needed, just marking current version
                
            elif op == "ROLLBACK":
                v = int(data[idx]); idx += 1
                pst.rollback(v)
        
        results.extend(case_results)
    
    return "\n".join(results)