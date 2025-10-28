import sys
sys.setrecursionlimit(300000)

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        
        self.min_tree = [10**18] * (2 * self.size)
        self.max_tree = [-10**18] * (2 * self.size)
        self.sum_tree = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        
        for i in range(self.n):
            self.min_tree[self.size + i] = data[i]
            self.max_tree[self.size + i] = data[i]
            self.sum_tree[self.size + i] = data[i]
        
        for i in range(self.size - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[2*i], self.min_tree[2*i+1])
            self.max_tree[i] = max(self.max_tree[2*i], self.max_tree[2*i+1])
            self.sum_tree[i] = self.sum_tree[2*i] + self.sum_tree[2*i+1]
    
    def _apply(self, i, val, length):
        self.min_tree[i] += val
        self.max_tree[i] += val
        self.sum_tree[i] += val * length
        if i < self.size:
            self.lazy[i] += val
    
    def _push(self, i, length):
        if self.lazy[i] != 0:
            left_len = length // 2
            right_len = length - left_len
            self._apply(2*i, self.lazy[i], left_len)
            self._apply(2*i+1, self.lazy[i], right_len)
            self.lazy[i] = 0
    
    def _update(self, l, r, val, i, segL, segR):
        if r < segL or segR < l:
            return
        
        length = segR - segL + 1
        
        if l <= segL and segR <= r:
            self._apply(i, val, length)
            return
        
        self._push(i, length)
        mid = (segL + segR) // 2
        self._update(l, r, val, 2*i, segL, mid)
        self._update(l, r, val, 2*i+1, mid+1, segR)
        
        self.min_tree[i] = min(self.min_tree[2*i], self.min_tree[2*i+1])
        self.max_tree[i] = max(self.max_tree[2*i], self.max_tree[2*i+1])
        self.sum_tree[i] = self.sum_tree[2*i] + self.sum_tree[2*i+1]
    
    def update_range(self, l, r, val):
        self._update(l, r, val, 1, 0, self.size-1)
    
    def _query_min(self, l, r, i, segL, segR):
        if r < segL or segR < l:
            return 10**18
        
        if l <= segL and segR <= r:
            return self.min_tree[i]
        
        length = segR - segL + 1
        self._push(i, length)
        mid = (segL + segR) // 2
        left_min = self._query_min(l, r, 2*i, segL, mid)
        right_min = self._query_min(l, r, 2*i+1, mid+1, segR)
        return min(left_min, right_min)
    
    def query_min(self, l, r):
        return self._query_min(l, r, 1, 0, self.size-1)
    
    def _query_max(self, l, r, i, segL, segR):
        if r < segL or segR < l:
            return -10**18
        
        if l <= segL and segR <= r:
            return self.max_tree[i]
        
        length = segR - segL + 1
        self._push(i, length)
        mid = (segL + segR) // 2
        left_max = self._query_max(l, r, 2*i, segL, mid)
        right_max = self._query_max(l, r, 2*i+1, mid+1, segR)
        return max(left_max, right_max)
    
    def query_max(self, l, r):
        return self._query_max(l, r, 1, 0, self.size-1)
    
    def _query_sum(self, l, r, i, segL, segR):
        if r < segL or segR < l:
            return 0
        
        if l <= segL and segR <= r:
            return self.sum_tree[i]
        
        length = segR - segL + 1
        self._push(i, length)
        mid = (segL + segR) // 2
        left_sum = self._query_sum(l, r, 2*i, segL, mid)
        right_sum = self._query_sum(l, r, 2*i+1, mid+1, segR)
        return left_sum + right_sum
    
    def query_sum(self, l, r):
        return self._query_sum(l, r, 1, 0, self.size-1)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); Q = int(data[idx+1]); idx += 2
    arr = list(map(int, data[idx:idx+N])); idx += N
    
    seg_tree = SegmentTree(arr)
    results = []
    
    for _ in range(Q):
        op = data[idx]; idx += 1
        if op == "UPDATE":
            l = int(data[idx]); r = int(data[idx+1]); val = int(data[idx+2]); idx += 3
            seg_tree.update_range(l, r, val)
        elif op == "QUERY_MIN":
            l = int(data[idx]); r = int(data[idx+1]); idx += 2
            result = seg_tree.query_min(l, r)
            results.append(str(result))
        elif op == "QUERY_MAX":
            l = int(data[idx]); r = int(data[idx+1]); idx += 2
            result = seg_tree.query_max(l, r)
            results.append(str(result))
        elif op == "QUERY_SUM":
            l = int(data[idx]); r = int(data[idx+1]); idx += 2
            result = seg_tree.query_sum(l, r)
            results.append(str(result))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()