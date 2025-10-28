import unittest
from solution import can_color_graph


class TestGraphColoring(unittest.TestCase):

    def test_empty_graph(self):
        """Empty graph should be colorable with any k >= 0."""
        self.assertTrue(can_color_graph({}, 1))
        self.assertTrue(can_color_graph({}, 3))
        self.assertTrue(can_color_graph({}, 0))  # Edge: empty + 0 colors = True


    def test_single_vertex(self):
        """Single vertex is always colorable with k >= 1."""
        graph = {0: []}
        self.assertTrue(can_color_graph(graph, 1))
        self.assertTrue(can_color_graph(graph, 2))
        self.assertFalse(can_color_graph(graph, 0))

    def test_two_adjacent_vertices(self):
        """Two connected vertices need at least 2 colors."""
        graph = {0: [1], 1: [0]}
        self.assertTrue(can_color_graph(graph, 2))
        self.assertFalse(can_color_graph(graph, 1))

    def test_triangle_complete_graph(self):
        """Triangle (K3) needs exactly 3 colors."""
        graph = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1]
        }
        self.assertTrue(can_color_graph(graph, 3))
        self.assertFalse(can_color_graph(graph, 2))

    def test_bipartite_graph(self):
        """Bipartite graph (e.g., square) is 2-colorable."""
        graph = {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
        self.assertTrue(can_color_graph(graph, 2))
        self.assertTrue(can_color_graph(graph, 3))

    def test_disconnected_components(self):
        """Disconnected components: each must be colorable."""
        # Two separate edges: each needs 2 colors, so overall 2 colors suffice
        graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2]
        }
        self.assertTrue(can_color_graph(graph, 2))
        self.assertFalse(can_color_graph(graph, 1))  # 1 color not enough

    def test_four_node_clique(self):
        """Complete graph K4 needs exactly 4 colors."""
        graph = {
            0: [1, 2, 3],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [0, 1, 2]
        }
        self.assertTrue(can_color_graph(graph, 4))
        self.assertFalse(can_color_graph(graph, 3))

    def test_linear_chain(self):
        """Linear chain (path graph) is 2-colorable."""
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
        self.assertTrue(can_color_graph(graph, 2))
        self.assertFalse(can_color_graph(graph, 1))  # Needs at least 2 colors


    def test_isolated_vertices(self):
        """Graph with isolated vertices (no edges) → 1 color suffices."""
        graph = {
            0: [],
            1: [],
            2: []
        }
        self.assertTrue(can_color_graph(graph, 1))
        self.assertTrue(can_color_graph(graph, 2))

    def test_star_graph(self):
        """Star graph (one center connected to all others) → 2-colorable."""
        graph = {
            0: [1, 2, 3],  # Center
            1: [0],
            2: [0],
            3: [0]
        }
        self.assertTrue(can_color_graph(graph, 2))
        self.assertFalse(can_color_graph(graph, 1))

    def test_odd_cycle(self):
        """Odd cycle (e.g., pentagon) needs 3 colors."""
        graph = {
            0: [1, 4],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [0, 3]
        }  # 5-node cycle (odd)
        self.assertTrue(can_color_graph(graph, 3))
        self.assertFalse(can_color_graph(graph, 2))


    def test_even_cycle(self):
        """Even cycle (e.g., hexagon) is 2-colorable."""
        graph = {
            0: [1, 5],
            1: [0, 2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [0, 4]
        }  # 6-node cycle (even)
        self.assertTrue(can_color_graph(graph, 2))
        self.assertTrue(can_color_graph(graph, 3))

    def test_k_greater_than_vertices(self):
        """If k >= number of vertices, always colorable (assign unique colors)."""
        graph = {0: [1], 1: [0]}  # 2 vertices
        self.assertTrue(can_color_graph(graph, 3))  # k=3 > 2 vertices

    def test_zero_colors_nonempty(self):
        """Non-empty graph with k=0 → always False."""
        graph = {0: [1], 1: [0]}
        self.assertFalse(can_color_graph(graph, 0))


if __name__ == '__main__':
    unittest.main()
