import unittest
from solution import find_critical_node_components

class TestGraphConnectivity(unittest.TestCase):

    def test_basic_critical_nodes(self):
        """Test case with clear critical nodes."""
        n = 5
        edges = [(0,1), (1,2), (2,0), (1,3), (3,4)]
        result = find_critical_node_components(n, edges)
        self.assertEqual(result, [(1, 2), (3, 2)])

    def test_no_critical_nodes(self):
        """Test a cycle graph (no articulation points)."""
        n = 4
        edges = [(0,1), (1,2), (2,3), (3,0)]
        result = find_critical_node_components(n, edges)
        self.assertEqual(result, [])

    def test_single_node(self):
        """Test single node graph."""
        n = 1
        edges = []
        result = find_critical_node_components(n, edges)
        self.assertEqual(result, [])  # No critical node possible

    def test_disconnected_graph(self):
        """
        Test initially disconnected graph with two separate triangles.
        Expected: No critical nodes (each triangle is 2-connected).
        """
        n = 6
        edges = [(0,1), (1,2), (2,0), (3,4), (4,5), (5,3)]  # Two triangles
        result = find_critical_node_components(n, edges)
        self.assertEqual(result, [])  # Both components are cycles → no articulation points


    def test_tree_structure(self):
        """
        Test a tree (every non-leaf node is critical).
        Graph: 0-1-2-3, and 1-4 (star-like)
        Critical nodes: 1 (removal splits into 3 components), 2 (splits into 2)
        """
        n = 5
        edges = [(0,1), (1,2), (2,3), (1,4)]
        result = find_critical_node_components(n, edges)
        # Node 1 removal → 3 components: {0}, {2,3}, {4}
        # Node 2 removal → 2 components: {0,1,4}, {3}
        self.assertEqual(result, [(1, 3), (2, 2)])

    def test_isolated_nodes(self):
        """
        Test graph with isolated nodes and a connected component.
        Nodes 0,1,2 form a triangle; 3 and 4 are isolated.
        No critical nodes (triangle has none, isolated nodes can't be articulation points).
        """
        n = 5
        edges = [(0,1), (1,2), (2,0)]  # Triangle + 2 isolated nodes
        result = find_critical_node_components(n, edges)
        self.assertEqual(result, [])

    def test_linear_chain(self):
        """
        Test a linear chain (every internal node is critical).
        Graph: 0-1-2-3-4
        Critical nodes: 1,2,3 (removal increases components)
        """
        n = 5
        edges = [(0,1), (1,2), (2,3), (3,4)]
        result = find_critical_node_components(n, edges)
        # Removing 1 → {0}, {2,3,4} → 2 components
        # Removing 2 → {0,1}, {3,4} → 2 components  
        # Removing 3 → {0,1,2}, {4} → 2 components
        self.assertEqual(result, [(1, 2), (2, 2), (3, 2)])


    def test_fully_connected(self):
        """
        Test a fully connected graph (clique) - no articulation points.
        Any node removal keeps graph connected.
        """
        n = 4
        # All possible edges in K4
        edges = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
        result = find_critical_node_components(n, edges)
        self.assertEqual(result, [])  # K4 has no articulation points


    def test_two_nodes_single_edge(self):
        """
        Test two nodes connected by a single edge.
        Both nodes are articulation points (removal disconnects the graph).
        """
        n = 2
        edges = [(0,1)]
        result = find_critical_node_components(n, edges)
        # Remove 0 → {1} → 1 component (but original was 1, so increase?)
        # Actually: original has 1 component; after removal: 1 isolated node → still 1 component?
        # Correction: removal of either node leaves 1 node → 1 component. 
        # But articulation point definition: increases number of components.
        # Original: 1 component; After: 1 component → no increase → not articulation!
        # So no critical nodes.
        self.assertEqual(result, [])

    def test_complex_graph_with_bridges(self):
        """
        Test a graph with bridges and multiple articulation points.
        Structure:
          0-1-2-3
            |
            4-5
        Critical nodes: 1 (connects 0 to rest), 2 (bridge between 1 and 3), 4 (connects to 5)
        """
        n = 6
        edges = [(0,1), (1,2), (2,3), (1,4), (4,5)]
        result = find_critical_node_components(n, edges)
        # Remove 1 → components: {0}, {2,3}, {4,5} → 3
        # Remove 2 → components: {0,1,4,5}, {3} → 2
        # Remove 4 → components: {0,1,2,3}, {5} → 2
        self.assertEqual(result, [(1, 3), (2, 2), (4, 2)])


if __name__ == "__main__":
    unittest.main()
