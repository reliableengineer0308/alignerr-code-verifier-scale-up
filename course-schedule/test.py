import unittest
from solution import canFinish

class TestCourseSchedule(unittest.TestCase):
    def test_simple_case(self):
        self.assertTrue(canFinish(2, [[1, 0]]))

    def test_cycle(self):
        self.assertFalse(canFinish(2, [[1, 0], [0, 1]]))

    def test_no_prerequisites(self):
        self.assertTrue(canFinish(3, []))

    def test_linear_chain(self):
        self.assertTrue(canFinish(4, [[1, 0], [2, 1], [3, 2]]))

    def test_fork(self):
        self.assertTrue(canFinish(3, [[1, 0], [2, 0]]))  # 0 → 1 and 0 → 2

    def test_join(self):
        self.assertTrue(canFinish(3, [[2, 0], [2, 1]]))  # 0→2 and 1→2

    def test_multiple_cycles(self):
        self.assertFalse(canFinish(4, [[0,1],[1,2],[2,3],[3,1]]))  # 1→2→3→1

    def test_single_course(self):
        self.assertTrue(canFinish(1, []))

    def test_disconnected_components(self):
        self.assertTrue(canFinish(5, [[1,0], [3,2]]))  # Two separate chains

    def test_self_loop(self):
        self.assertFalse(canFinish(1, [[0,0]]))  # Course requires itself

if __name__ == '__main__':
    unittest.main()
