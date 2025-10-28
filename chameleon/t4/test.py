import unittest
import sys
from io import StringIO
from solution import solve_tsp

class TestTSP(unittest.TestCase):
    
    def test_sample_case(self):
        dist = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        
        cost, path = solve_tsp(dist)
        
        self.assertEqual(cost, 80)
        self.assertEqual(len(path), 5)  # Includes return to start
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 0)
    
    def test_three_cities(self):
        dist = [
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0]
        ]
        
        cost, path = solve_tsp(dist)
        
        self.assertEqual(cost, 6)  # 0->1->2->0: 1 + 3 + 2 = 6
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 0)
    
    def test_no_path(self):
        dist = [
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 0]
        ]
        
        result, path = solve_tsp(dist)
        
        self.assertEqual(result, "No path exists")
        self.assertEqual(path, [])
    
    def test_asymmetric_tsp(self):
        dist = [
            [0, 1, 2],
            [3, 0, 4],
            [5, 6, 0]
        ]
        
        cost, path = solve_tsp(dist)
        
        # Should find a valid path
        self.assertNotEqual(cost, 10**9)
        self.assertEqual(len(path), 4)  # Includes return to start
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 0)

if __name__ == '__main__':
    unittest.main()