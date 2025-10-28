import sys
sys.setrecursionlimit(300000)

class SplayNode:
    __slots__ = ('val', 'sum', 'size', 'left', 'right', 'parent')
    def __init__(self, val):
        self.val = val
        self.sum = val
        self.size = 1
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None
    
    def update(self, node):
        if node is None:
            return
        node.size = 1
        node.sum = node.val
        if node.left is not None:
            node.size += node.left.size
            node.sum += node.left.sum
        if node.right is not None:
            node.size += node.right.size
            node.sum += node.right.sum
    
    def rotate(self, x):
        p = x.parent
        g = p.parent if p is not None else None
        
        if p is not None:
            if p.left == x:
                p.left = x.right
                if x.right is not None:
                    x.right.parent = p
                x.right = p
            else:
                p.right = x.left
                if x.left is not None:
                    x.left.parent = p
                x.left = p
            
            x.parent = g
            p.parent = x
            
            if g is not None:
                if g.left == p:
                    g.left = x
                else:
                    g.right = x
            
            self.update(p)
            self.update(x)
    
    def splay(self, x):
        while x.parent is not None:
            p = x.parent
            g = p.parent
            
            if g is None:
                self.rotate(x)
            else:
                if (g.left == p) == (p.left == x):
                    self.rotate(p)
                    self.rotate(x)
                else:
                    self.rotate(x)
                    self.rotate(x)
        
        self.root = x
    
    def find_by_index(self, idx):
        node = self.root
        while node is not None:
            left_size = node.left.size if node.left is not None else 0
            if idx < left_size:
                node = node.left
            elif idx == left_size:
                self.splay(node)
                return node
            else:
                idx -= left_size + 1
                node = node.right
        return None
    
    def split(self, idx):
        if idx == 0:
            left = None
            right = self.root
            if right is not None:
                right.parent = None
            return left, right
        
        node = self.find_by_index(idx - 1)
        if node is None:
            return self.root, None
        
        self.splay(node)
        right = node.right
        node.right = None
        if right is not None:
            right.parent = None
        self.update(node)
        return node, right
    
    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        node = left
        while node.right is not None:
            node = node.right
        self.splay(node)
        node.right = right
        right.parent = node
        self.update(node)
        return node
    
    def insert(self, idx, val):
        new_node = SplayNode(val)
        if self.root is None:
            self.root = new_node
            return
        
        if idx == 0:
            new_node.right = self.root
            self.root.parent = new_node
            self.root = new_node
            self.update(new_node)
            return
        
        left, right = self.split(idx)
        new_node.left = left
        new_node.right = right
        if left is not None:
            left.parent = new_node
        if right is not None:
            right.parent = new_node
        self.update(new_node)
        self.root = new_node
    
    def delete(self, idx):
        node = self.find_by_index(idx)
        if node is None:
            return
        
        left = node.left
        right = node.right
        
        if left is not None:
            left.parent = None
        if right is not None:
            right.parent = None
        
        self.root = self.merge(left, right)
    
    def update_val(self, idx, val):
        node = self.find_by_index(idx)
        if node is not None:
            node.val = val
            self.update(node)
    
    def query_range(self, l, r):
        if l > r:
            return 0
        
        if l == 0:
            if r == self.root.size - 1:
                return self.root.sum if self.root is not None else 0
            
            node = self.find_by_index(r + 1)
            left = node.left
            return left.sum if left is not None else 0
        else:
            left1, right1 = self.split(l)
            left2, right2 = self.split(r - l + 1)
            result = left2.sum if left2 is not None else 0
            self.root = self.merge(self.merge(left1, left2), right2)
            return result

def solve_splay_tree():
    input = sys.stdin.read().split()
    idx = 0
    
    n = int(input[idx]); q = int(input[idx+1]); idx += 2
    arr = []
    for i in range(n):
        arr.append(int(input[idx])); idx += 1
    
    splay = SplayTree()
    for i, val in enumerate(arr):
        splay.insert(i, val)
    
    results = []
    
    for _ in range(q):
        op = input[idx]; idx += 1
        if op == "INSERT":
            i = int(input[idx]); x = int(input[idx+1]); idx += 2
            splay.insert(i, x)
        elif op == "DELETE":
            i = int(input[idx]); idx += 1
            splay.delete(i)
        elif op == "UPDATE":
            i = int(input[idx]); x = int(input[idx+1]); idx += 2
            splay.update_val(i, x)
        else:  # QUERY
            l = int(input[idx]); r = int(input[idx+1]); idx += 2
            result = splay.query_range(l, r)
            results.append(str(result))
    
    return results

if __name__ == "__main__":
    results = solve_splay_tree()
    for result in results:
        print(result)