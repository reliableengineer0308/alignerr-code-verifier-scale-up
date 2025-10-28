import unittest
from solution import minimizeTotalDelay

class TestResourceAllocation(unittest.TestCase):
    def test_example_1(self):
        n, m = 3, 2
        processing_time = [4, 6, 8]
        dependencies = [[], [0], [1]]
        self.assertEqual(minimizeTotalDelay(n, m, processing_time, dependencies), 9)

    def test_example_2(self):
        n, m = 2, 3
        processing_time = [10, 10]
        dependencies = [[], []]
        self.assertEqual(minimizeTotalDelay(n, m, processing_time, dependencies), 4)


    def test_example_3(self):
        n, m = 4, 2
        processing_time = [5, 3, 4, 7]
        dependencies = [[], [], [0, 1], [2]]
        self.assertEqual(minimizeTotalDelay(n, m, processing_time, dependencies), 9)


    def test_single_task(self):
        self.assertEqual(minimizeTotalDelay(1, 5, [10], [[]]), 2)  # ceil(10/5)=2


    def test_no_dependencies(self):
        n, m = 3, 1
        processing_time = [2, 3, 4]
        dependencies = [[], [], []]
        self.assertEqual(minimizeTotalDelay(n, m, processing_time, dependencies), 4)

    def test_full_parallel(self):
        n, m = 5, 10
        processing_time = [8] * 5
        dependencies = [[] for _ in range(5)]
        # Each runs in ceil(8/10)=1 → all finish at 1
        self.assertEqual(minimizeTotalDelay(n, m, processing_time, dependencies), 1)

if __name__ == '__main__':
    unittest.main()
