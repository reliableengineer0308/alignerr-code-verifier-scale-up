class SegmentTree:
    def __init__(self, data):
        """Initialize segment tree with data array."""
        self.n = len(data)
        if self.n == 0:
            self.tree = []
            self.lazy = []
            return

        # Allocate 4*n for safety (standard size for segment trees)
        self.tree = [0] * (4 * self.n)  # Stores range sums
        self.lazy = [0] * (4 * self.n)  # Pending updates (lazy values)

        self._build(data, 0, self.n - 1, 1)

    def _build(self, data, l, r, node):
        """Build tree from data[l..r] at node."""
        if l == r:
            self.tree[node] = data[l]
            return
        mid = (l + r) // 2
        self._build(data, l, mid, node * 2)
        self._build(data, mid + 1, r, node * 2 + 1)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _propagate(self, node, l, r):
        """Propagate pending updates to children."""
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            left_node, right_node = node * 2, node * 2 + 1

            # Update left child: add lazy value × number of elements in left segment
            self.tree[left_node] += self.lazy[node] * (mid - l + 1)
            self.lazy[left_node] += self.lazy[node]

            # Update right child: add lazy value × number of elements in right segment
            self.tree[right_node] += self.lazy[node] * (r - mid)
            self.lazy[right_node] += self.lazy[node]

            # Clear lazy value at current node
            self.lazy[node] = 0

    def update(self, l, r, val):
        """Add val to all elements in range [l, r] (0-based)."""
        if self.n == 0 or l > r or l < 0 or r >= self.n:
            return
        self._update_range(l, r, val, 0, self.n - 1, 1)

    def _update_range(self, ul, ur, val, l, r, node):
        """Internal method to update range [ul, ur] with val."""
        # No overlap
        if ur < l or ul > r:
            return

        # Full overlap: update current node and set lazy
        if ul <= l and r <= ur:
            self.tree[node] += val * (r - l + 1)
            self.lazy[node] += val
            return

        # Partial overlap: propagate pending updates and recurse
        self._propagate(node, l, r)
        mid = (l + r) // 2
        self._update_range(ul, ur, val, l, mid, node * 2)
        self._update_range(ul, ur, val, mid + 1, r, node * 2 + 1)
        # Update current node after children are updated
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query_point(self, idx):
        """Get value at index idx (0-based)."""
        if self.n == 0 or idx < 0 or idx >= self.n:
            return 0
        return self._query_point(idx, 0, self.n - 1, 1)

    def _query_point(self, idx, l, r, node):
        """Internal method to query a single point."""
        if l == r:
            return self.tree[node]
        self._propagate(node, l, r)
        mid = (l + r) // 2
        if idx <= mid:
            return self._query_point(idx, l, mid, node * 2)
        else:
            return self._query_point(idx, mid + 1, r, node * 2 + 1)

    def query_range(self, l, r):
        """Return sum over range [l, r] (0-based)."""
        if self.n == 0 or l > r or l < 0 or r >= self.n:
            return 0
        return self._query_range(l, r, 0, self.n - 1, 1)


    def _query_range(self, ql, qr, l, r, node):
        """Internal method to query range sum."""
        # No overlap
        if qr < l or ql > r:
            return 0
        # Full overlap
        if ql <= l and r <= qr:
            return self.tree[node]
        # Partial overlap: propagate and recurse
        self._propagate(node, l, r)
        mid = (l + r) // 2
        left_sum = self._query_range(ql, qr, l, mid, node * 2)
        right_sum = self._query_range(ql, qr, mid + 1, r, node * 2 + 1)
        return left_sum + right_sum
