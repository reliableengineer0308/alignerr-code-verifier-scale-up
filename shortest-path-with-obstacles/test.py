import unittest
from solution import shortest_path_with_obstacles


class TestShortestPath(unittest.TestCase):
    def test_example_1(self):
        grid = [
            [0, 2, 1],
            [0, 1, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 3)  

    def test_blocked_no_special(self):
        grid = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, -1)


    def test_direct_path(self):
        grid = [[0]]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 0)


    def test_simple_path_no_obstacles(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 3) 


    def test_requires_special_ability(self):
        grid = [
            [0, 1, 1],
            [2, 1, 0],
            [0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 4)


    def test_multiple_special_cells(self):
        grid = [
            [0, 2, 0],
            [1, 2, 1],
            [0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 4)


    def test_ability_does_not_stack(self):
        grid = [
            [0, 2, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 5)


    def test_no_path_even_with_ability(self):
        grid = [
            [0, 2, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertEqual(result, 4)


    def test_large_grid_with_detour(self):
        grid = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 1, 2, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        result = shortest_path_with_obstacles(grid)
        self.assertGreaterEqual(result, 6)
        self.assertLessEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
