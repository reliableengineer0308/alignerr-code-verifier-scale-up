import unittest
from solution import SegmentTree

class TestSegmentTree(unittest.TestCase):
    
    def test_empty_array(self):
        """Test behavior with empty array."""
        st = SegmentTree([])
        self.assertEqual(st.query_point(0), 0)
        self.assertEqual(st.query_range(0, 1), 0)
        st.update(0, 1, 5)  # Should not raise errors


    def test_single_element(self):
        """Test single-element array."""
        st = SegmentTree([10])
        self.assertEqual(st.query_point(0), 10)
        self.assertEqual(st.query_range(0, 0), 10)
        
        st.update(0, 0, 3)
        self.assertEqual(st.query_point(0), 13)
        self.assertEqual(st.query_range(0, 0), 13)


    def test_initial_build(self):
        """Test correct tree construction from initial array."""
        arr = [1, 3, 5, 7]
        st = SegmentTree(arr)
        self.assertEqual(st.query_range(0, 3), 16)  # 1+3+5+7
        self.assertEqual(st.query_point(2), 5)
        self.assertEqual(st.query_range(1, 2), 8)   # 3+5

    def test_range_update(self):
        """Test range update functionality."""
        arr = [0, 0, 0, 0]
        st = SegmentTree(arr)
        
        st.update(1, 2, 5)  # [0,5,5,0]
        self.assertEqual(st.query_range(1, 2), 10)
        self.assertEqual(st.query_point(1), 5)
        self.assertEqual(st.query_point(3), 0)
        self.assertEqual(st.query_range(0, 3), 10)

    def test_multiple_updates(self):
        """Test multiple overlapping updates."""
        st = SegmentTree([1, 2, 3, 4])
        
        st.update(0, 3, 2)  # [3,4,5,6]
        st.update(1, 2, -1) # [3,3,4,6]
        
        self.assertEqual(st.query_range(0, 3), 16)
        self.assertEqual(st.query_point(1), 3)
        self.assertEqual(st.query_point(2), 4)

        self.assertEqual(st.query_range(2, 3), 10)  # 4+6

    def test_partial_overlap_updates(self):
        """Test updates with partial range overlap."""
        st = SegmentTree([10, 20, 30, 40])
        
        st.update(1, 3, 5)  # [10,25,35,45]
        self.assertEqual(st.query_range(0, 1), 35)   # 10+25
        self.assertEqual(st.query_range(2, 3), 80)   # 35+45
        self.assertEqual(st.query_point(3), 45)


    def test_edge_cases_queries(self):
        """Test queries with edge-case ranges."""
        st = SegmentTree([5, 10, 15])
        
        # Out-of-bounds queries should return 0
        self.assertEqual(st.query_range(-1, 0), 0)    # Clamped to [0,0]
        self.assertEqual(st.query_range(2, 5), 0)     # Clamped to [2,2]
        self.assertEqual(st.query_point(-1), 0)         # Invalid index
        self.assertEqual(st.query_point(5), 0)       # Invalid index


    def test_negative_values(self):
        """Test handling of negative numbers."""
        st = SegmentTree([-1, -2, -3])
        
        self.assertEqual(st.query_range(0, 2), -6)
        st.update(0, 1, 4)  # [3,2,-3]
        self.assertEqual(st.query_range(0, 1), 5)
        self.assertEqual(st.query_point(2), -3)


    def test_large_updates(self):
        """Test large update values."""
        st = SegmentTree([0, 0])
        st.update(0, 1, 10**9)
        self.assertEqual(st.query_range(0, 1), 2 * 10**9)
        self.assertEqual(st.query_point(0), 10**9)


    def test_sequential_updates(self):
        """Test repeated updates to same range."""
        st = SegmentTree([1, 1, 1])
        
        for _ in range(5):
            st.update(0, 2, 1)  # Add 1 each time
        
        self.assertEqual(st.query_range(0, 2), 3 + 5 * 3)  # Initial 3 + 15 from updates
        self.assertEqual(st.query_point(1), 6)


if __name__ == '__main__':
    unittest.main()
