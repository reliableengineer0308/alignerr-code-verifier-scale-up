import unittest
import sys
from io import StringIO
from solution import dijkstra

class TestDijkstra(unittest.TestCase):
    
    def test_sample_case(self):
        n = 5
        edges = [
            (0, 1, 4),
            (0, 2, 1),
            (1, 3, 1),
            (2, 1, 2),
            (2, 3, 5),
            (3, 4, 3),
            (2, 4, 10)
        ]
        S, T = 0, 4
        
        distance, path = dijkstra(n, edges, S, T)
        
        self.assertEqual(distance, 7)
        self.assertEqual(path, [0, 2, 1, 3, 4])
    
    def test_no_path(self):
        n = 3
        edges = [
            (0, 1, 1),
            # No path from 0 to 2
        ]
        S, T = 0, 2
        
        distance, path = dijkstra(n, edges, S, T)
        
        self.assertEqual(distance, -1)
        self.assertEqual(path, [])
    
    def test_direct_path(self):
        n = 3
        edges = [
            (0, 1, 5),
            (0, 2, 10),
            (1, 2, 3)
        ]
        S, T = 0, 2
        
        distance, path = dijkstra(n, edges, S, T)
        
        # Should take 0→1→2: 5 + 3 = 8
        self.assertEqual(distance, 8)
        self.assertEqual(path, [0, 1, 2])
    
    def test_same_start_end(self):
        n = 3
        edges = [
            (0, 1, 5),
            (1, 2, 3)
        ]
        S, T = 0, 0
        
        distance, path = dijkstra(n, edges, S, T)
        
        self.assertEqual(distance, 0)
        self.assertEqual(path, [0])

if __name__ == '__main__':
    unittest.main()