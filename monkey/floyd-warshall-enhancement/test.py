import unittest
from solution import floyd_warshall_enhanced, get_path



class TestFloydWarshallEnhanced(unittest.TestCase):

    def test_single_vertex(self):
        """Test graph with one vertex."""
        graph = [[0]]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)
        self.assertEqual(distances, [[0]])
        self.assertEqual(parents, [[None]])
        self.assertFalse(has_cycle)

    def test_no_edges(self):
        """Test disconnected graph (no edges)."""
        graph = [
            [0, float('inf'), float('inf')],
            [float('inf'), 0, float('inf')],
            [float('inf'), float('inf'), 0]
        ]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)
        self.assertEqual(distances, graph)
        self.assertTrue(all(
            parents[i][j] is None
            for i in range(3)
            for j in range(3)
            if i != j
        ))
        self.assertFalse(has_cycle)

    def test_basic_positive_weights(self):
        """Test simple graph with positive weights."""
        graph = [
            [0, 3, float('inf'), 7],
            [8, 0, 2, float('inf')],
            [5, float('inf'), 0, 1],
            [2, float('inf'), float('inf'), 0]
        ]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)

        # Known shortest path: 0->1->2 = 3+2 = 5
        self.assertEqual(distances[0][2], 5)

        # Path reconstruction: 0 -> 1 -> 2
        path = get_path(parents, 0, 2)
        self.assertEqual(path, [0, 1, 2])

        # Check other known distances
        self.assertEqual(distances[3][0], 2)  # Direct edge
        self.assertEqual(distances[0][3], 6)  # 0->1->2->3 = 3+2+1

        self.assertFalse(has_cycle)

    def test_negative_weights_no_cycle(self):
        """Test graph with negative weights but no negative cycles."""
        graph = [
            [0, -2, float('inf')],
            [4, 0, 3],
            [float('inf'), 7, 0]
        ]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)

        # 0->1 is -2 (direct)
        self.assertEqual(distances[0][1], -2)

        # 0->1->2 = -2 + 3 = 1
        self.assertEqual(distances[0][2], 1)
        # 1->0 should be 4 (direct), not improved via 1->2->0 (4 vs 3+7=10)
        self.assertEqual(distances[1][0], 4)


        path = get_path(parents, 0, 2)
        self.assertEqual(path, [0, 1, 2])


        self.assertFalse(has_cycle)

    def test_negative_cycle(self):
        """Test graph with a negative cycle."""
        # Cycle: 1->2->1 with weights -3 and 1 → total -2 (negative cycle)
        graph = [
            [0, 1, float('inf')],
            [float('inf'), 0, -3],
            [float('inf'), 1, 0]
        ]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)


        self.assertTrue(has_cycle)
        # After negative cycle, some distances may become nonsensical
        # But algorithm should detect the cycle


    def test_disconnected_components(self):
        """Test graph with disconnected components."""
        graph = [
            [0, 5, float('inf'), float('inf')],
            [float('inf'), 0, float('inf'), float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)


        # Component 1: 0<->1
        self.assertEqual(distances[0][1], 5)
        self.assertEqual(distances[1][0], float('inf'))  # No reverse edge


        # Component 2: 2<->3
        self.assertEqual(distances[2][3], 1)
        self.assertEqual(distances[3][2], float('inf'))


        # No path between components
        self.assertEqual(distances[0][2], float('inf'))
        self.assertEqual(distances[3][1], float('inf'))


        self.assertFalse(has_cycle)


    def test_self_loops(self):
        """Test graph with self-loops (should be ignored)."""
        graph = [
            [1, 2],  # Self-loop with weight 1 (should become 0 in result)
            [3, -1]  # Self-loop with weight -1 (negative cycle!)
        ]
        distances, parents, has_cycle = floyd_warshall_enhanced(graph)


        # Floyd-Warshall sets diagonal to 0
        self.assertEqual(distances[0][0], 0)
        self.assertEqual(distances[1][1], 0)  


        # Negative self-loop creates negative cycle
        self.assertFalse(has_cycle)


    def test_large_graph(self):
        """Stress test with larger graph (n=50)."""
        n = 50
        # Create a chain graph: i -> i+1 with weight 1
        graph = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
            if i < n - 1:
                graph[i][i + 1] = 1


        distances, parents, has_cycle = floyd_warshall_enhanced(graph)


        # Distance from 0 to 49 should be 49
        self.assertEqual(distances[0][49], 49)


        # Path should be 0->1->...->49
        path = get_path(parents, 0, 49)
        expected = list(range(50))
        self.assertEqual(path, expected)


        self.assertFalse(has_cycle)


    def test_get_path_no_path(self):
        """Test path reconstruction when no path exists."""
        graph = [
            [0, float('inf')],
            [float('inf'), 0]
        ]
        distances, parents, _ = floyd_warshall_enhanced(graph)


        path = get_path(parents, 0, 1)
        self.assertEqual(path, [])  # No path exists

    def test_complete_graph(self):
        """Test fully connected graph."""
        n = 4
        graph = [[i + j for j in range(n)] for i in range(n)]  # Arbitrary weights
        for i in range(n):
            graph[i][i] = 0  # Ensure diagonal is 0

        distances, parents, has_cycle = floyd_warshall_enhanced(graph)


        # All pairs should have finite distances
        for i in range(n):
            for j in range(n):
                self.assertNotEqual(distances[i][j], float('inf'))


        self.assertFalse(has_cycle)

if __name__ == '__main__':
    unittest.main()
