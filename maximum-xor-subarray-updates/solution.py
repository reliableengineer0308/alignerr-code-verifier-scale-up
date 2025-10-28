import sys
sys.setrecursionlimit(300000)

class BinaryTrie:
    class Node:
        __slots__ = ['child', 'min_idx', 'max_idx']
        def __init__(self):
            self.child = [None, None]
            self.min_idx = float('inf')
            self.max_idx = -1
    
    def __init__(self, bits=32):
        self.root = self.Node()
        self.bits = bits
    
    def insert(self, x, idx):
        node = self.root
        node.min_idx = min(node.min_idx, idx)
        node.max_idx = max(node.max_idx, idx)
        
        for i in range(self.bits-1, -1, -1):
            bit = (x >> i) & 1
            if not node.child[bit]:
                node.child[bit] = self.Node()
            node = node.child[bit]
            node.min_idx = min(node.min_idx, idx)
            node.max_idx = max(node.max_idx, idx)
    
    def query_max_xor(self, x, l, r):
        node = self.root
        if node.min_idx > r or node.max_idx < l:
            return -1
            
        res = 0
        for i in range(self.bits-1, -1, -1):
            bit = (x >> i) & 1
            desired = 1 - bit
            
            if (node.child[desired] and 
                node.child[desired].min_idx <= r and 
                node.child[desired].max_idx >= l):
                res |= (1 << i)
                node = node.child[desired]
            else:
                node = node.child[bit]
        return res

class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [BinaryTrie() for _ in range(2 * self.size)]
        self.arr = arr
        
        # Build segment tree
        for i in range(n):
            self.tree[self.size + i].insert(arr[i], i)
        
        for i in range(self.size-1, 0, -1):
            self._merge(i)
    
    def _merge(self, idx):
        left = self.tree[2*idx]
        right = self.tree[2*idx+1]
        
        # Merge tries by inserting all elements from both children
        self.tree[idx] = BinaryTrie()
        
        # For simplicity, we'll reconstruct by querying ranges
        # In practice, you'd implement merge operation for tries
    
    def update(self, idx, val):
        pos = idx + self.size
        old_val = self.arr[idx]
        self.arr[idx] = val
        
        # Rebuild the leaf node
        self.tree[pos] = BinaryTrie()
        self.tree[pos].insert(val, idx)
        
        pos //= 2
        while pos:
            # Rebuild internal node
            self.tree[pos] = BinaryTrie()
            left_idx = 2*pos
            right_idx = 2*pos+1
            
            # Rebuild by collecting all indices in range
            # This is simplified - in practice you'd implement proper merging
            for i in range(self.tree[left_idx].min_idx, self.tree[left_idx].max_idx + 1):
                if i >= 0 and i < self.n:
                    self.tree[pos].insert(self.arr[i], i)
            for i in range(self.tree[right_idx].min_idx, self.tree[right_idx].max_idx + 1):
                if i >= 0 and i < self.n:
                    self.tree[pos].insert(self.arr[i], i)
            
            pos //= 2
    
    def query(self, l, r):
        # For maximum XOR subarray, we need prefix XOR
        # This is a simplified version
        prefix = [0] * (self.n + 1)
        for i in range(self.n):
            prefix[i+1] = prefix[i] ^ self.arr[i]
        
        max_xor = 0
        trie = BinaryTrie()
        trie.insert(0, 0)  # Insert prefix[0]
        
        for i in range(l, r + 1):
            if i > 0:
                trie.insert(prefix[i], i)
            max_xor = max(max_xor, trie.query_max_xor(prefix[i+1], l, i))
        
        return max_xor

def solve_max_xor_subarray():
    input_data = sys.stdin.read().split()
    if not input_data:
        return []
    
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input_data[idx]); q = int(input_data[idx+1]); idx += 2
        
        arr = []
        for _ in range(n):
            arr.append(int(input_data[idx])); idx += 1
        
        # Build prefix XOR array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        # For each position, we need to find max(prefix[i] ⊕ prefix[j]) for j < i
        # We'll use a global trie and handle updates by rebuilding
        
        case_results = [f"Case #{case_num}:"]
        
        # For simplicity, we'll handle queries naively for small cases
        # In practice, you'd use a more sophisticated data structure
        
        current_arr = arr.copy()
        current_prefix = prefix.copy()
        
        for _ in range(q):
            op = input_data[idx]; idx += 1
            
            if op == "UPDATE":
                i = int(input_data[idx]); x = int(input_data[idx+1]); idx += 2
                old_val = current_arr[i]
                current_arr[i] = x
                
                # Update prefix array
                for j in range(i, n):
                    current_prefix[j+1] = current_prefix[j] ^ current_arr[j]
                    
            else:  # QUERY
                l = int(input_data[idx]); r = int(input_data[idx+1]); idx += 2
                
                # Find max XOR subarray in [l, r]
                max_xor = 0
                trie = BinaryTrie()
                trie.insert(0, l)  # Insert prefix[l]
                
                for i in range(l, r + 1):
                    # prefix[i+1] is XOR from 0 to i
                    max_xor = max(max_xor, trie.query_max_xor(current_prefix[i+1], l, i))
                    trie.insert(current_prefix[i+1], i+1)
                
                case_results.append(str(max_xor))
        
        results.extend(case_results)
    
    return results