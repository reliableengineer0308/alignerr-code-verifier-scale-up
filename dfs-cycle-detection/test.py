import unittest
from solution import has_cycle

class TestDFSCycleDetection(unittest.TestCase):

    def test_empty_graph(self):
        """Test empty graph."""
        self.assertFalse(has_cycle({}))

    def test_single_node_no_edge(self):
        """Test single node with no edges."""
        graph = {"A": []}
        self.assertFalse(has_cycle(graph))


    def test_self_loop(self):
        """Test self-loop (cycle of length 1)."""
        graph = {"A": ["A"]}
        self.assertTrue(has_cycle(graph))


    def test_simple_cycle(self):
        """Test simple cycle: A → B → C → A."""
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertTrue(has_cycle(graph))


    def test_no_cycle(self):
        """Test acyclic graph: A → B → C."""
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": []
        }
        self.assertFalse(has_cycle(graph))


    def test_disconnected_components(self):
        """Test disconnected components with one cycle."""
        graph = {
            "A": ["B"],      # Acyclic component
            "B": [],
            "X": ["Y"],      # Cyclic component
            "Y": ["Z"],
            "Z": ["X"]
        }
        self.assertTrue(has_cycle(graph))


    def test_complex_graph_with_cycle(self):
        """Test complex graph with multiple paths and a cycle."""
        graph = {
            "0": ["1", "2"],
            "1": ["3"],
            "2": ["4"],
            "3": ["5"],
            "4": ["3"],  # Creates cycle: 3 → 5 → 4 → 3
            "5": ["4"]
        }
        self.assertTrue(has_cycle(graph))

    def test_large_acyclic_graph(self):
        """Stress test with large acyclic graph (chain)."""
        n = 100
        graph = {str(i): [str(i + 1)] for i in range(n)}
        graph[str(n)] = []  # Last node has no outgoing edge
        self.assertFalse(has_cycle(graph))


    def test_multiple_cycles(self):
        """Test graph with multiple independent cycles."""
        graph = {
            "A": ["B"],
            "B": ["A"],  # Cycle 1: A ⇄ B
            "X": ["Y"],
            "Y": ["Z"],
            "Z": ["X"]   # Cycle 2: X → Y → Z → X
        }
        self.assertTrue(has_cycle(graph))

if __name__ == '__main__':
    unittest.main()
