import unittest
from solution import shortestPathWithRestrictedEdges

class TestShortestPathWithRestrictedEdges(unittest.TestCase):

    def test_example_1(self):
        n = 4
        edges = [[0,1,2], [1,2,3], [2,3,4], [0,3,10]]
        restricted = [[1,2]]
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 3), 10)


    def test_example_2(self):
        n = 5
        edges = [[0,1,1], [1,2,2], [2,3,3], [3,4,4], [0,4,20]]
        restricted = [[1,2], [3,4]]
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 4), 20)

    def test_no_valid_path(self):
        n = 3
        edges = [[0,1,5], [1,2,10]]
        restricted = [[0,1], [1,2]]
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 2), -1)

    def test_direct_edge_available(self):
        n = 4
        edges = [[0,1,1], [1,2,1], [2,3,1], [0,3,1]]
        restricted = [[0,1], [1,2]]
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 3), 1)

    def test_start_equals_end(self):
        n = 2
        edges = [[0,1,5]]
        restricted = []
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 0), 0)

    def test_unconnected_graph(self):
        # Two separate components: 0-1 and 2-3. No path from 0 to 3.
        n = 4
        edges = [[0, 1, 1], [2, 3, 1]]
        restricted = []
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 3), -1)

    def test_single_node(self):
        # Only one node, start == end
        n = 1
        edges = []  # No edges needed
        restricted = []
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 0), 0)

    def test_no_edges(self):
        # Graph with nodes but no edges
        n = 3
        edges = []
        restricted = []
        # Start and end are different → no path
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 2), -1)
        # Start == end → distance 0
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 1, 1), 0)

    def test_all_edges_restricted(self):
        # All edges are blocked
        n = 3
        edges = [[0, 1, 5], [1, 2, 10], [0, 2, 15]]
        restricted = [[0, 1], [1, 2], [0, 2]]
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 2), -1)

    def test_multiple_paths_with_restrictions(self):
        # Complex graph with alternative routes
        n = 5
        edges = [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [0, 2, 7],  # Alternative path
            [0, 4, 20]  # Direct but expensive
        ]
        restricted = [[1, 2], [3, 4]]  # Block middle segments
        # Valid paths:
        # 0→2→3 (blocked at 3→4) → invalid
        # 0→1 (blocked at 1→2) → invalid
        # Only 0→4 remains
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 4), 20)

    def test_zero_weight_edges(self):
        # Edges with zero weight (allowed)
        n = 3
        edges = [[0, 1, 0], [1, 2, 0]]
        restricted = []
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 2), 0)

    def test_large_weights(self):
        # High edge weights
        n = 2
        edges = [[0, 1, 1000]]
        restricted = []
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 1), 1000)

    def test_restricted_edge_not_in_graph(self):
        # Restricted edge that doesn't exist in graph
        n = 3
        edges = [[0, 1, 1], [1, 2, 2]]
        restricted = [[0, 2]]  # This edge doesn't exist
        # Should work normally
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 2), 3)

    def test_bidirectional_restrictions(self):
        # Test that restriction (u,v) blocks both directions
        n = 3
        edges = [[0, 1, 5], [1, 2, 10]]
        restricted = [[1, 0]]  # Same as [0,1]
        # Path 0→1→2 should be blocked
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 2), -1)


    def test_many_nodes_sparse(self):
        # Large graph, sparse connections
        n = 100
        edges = []
        for i in range(0, 99, 2):  # Connect even nodes
            edges.append([i, i+1, 1])
        restricted = []
        # Check connectivity within component
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 98), -1)
        # Check unreachable node
        self.assertEqual(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 99), -1)

if __name__ == '__main__':
    unittest.main()
