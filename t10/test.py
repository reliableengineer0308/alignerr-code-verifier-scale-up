import unittest
import sys
from io import StringIO
from solution import solve_maze

class TestMazeBFS(unittest.TestCase):
    
    def test_sample_case(self):
        grid = [
            ['S', '.', '.', '#', '.'],
            ['#', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '#', '#', '#', '.'],
            ['.', '.', '.', 'T', '.']
        ]
        
        length, moves = solve_maze(grid)
        
        self.assertEqual(length, 9)
        self.assertEqual(len(moves), 9)
        self.assertEqual(moves, ['R', 'R', 'D', 'D', 'R', 'R', 'D', 'D', 'L'])
    
    def test_no_path(self):
        grid = [
            ['S', '#', '.'],
            ['#', '#', '.'],
            ['.', '#', 'T']
        ]
        
        length, moves = solve_maze(grid)
        
        self.assertEqual(length, -1)
        self.assertEqual(moves, [])
    
    def test_simple_case(self):
        grid = [
            ['S', '.', 'T']
        ]
        
        length, moves = solve_maze(grid)
        
        self.assertEqual(length, 2)
        self.assertEqual(moves, ['R', 'R'])
    
    def test_2x2_maze(self):
        grid = [
            ['S', '.'],
            ['.', 'T']
        ]
        
        length, moves = solve_maze(grid)
        
        self.assertEqual(length, 2)
        # Two possible shortest paths
        possible_paths = [['R', 'D'], ['D', 'R']]
        self.assertIn(moves, possible_paths)

if __name__ == '__main__':
    unittest.main()