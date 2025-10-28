import unittest
from solution import can_finish_courses

class TestCourseSchedule(unittest.TestCase):
    
    def test_no_cycle(self):
        num_courses = 4
        prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]
        self.assertTrue(can_finish_courses(num_courses, prerequisites))
    
    def test_with_cycle(self):
        num_courses = 2
        prerequisites = [(1, 0), (0, 1)]  # Cycle
        self.assertFalse(can_finish_courses(num_courses, prerequisites))
    
    def test_no_prerequisites(self):
        num_courses = 3
        prerequisites = []
        self.assertTrue(can_finish_courses(num_courses, prerequisites))
    
    def test_single_course(self):
        num_courses = 1
        prerequisites = []
        self.assertTrue(can_finish_courses(num_courses, prerequisites))
    
    def test_disconnected_graph(self):
        num_courses = 4
        prerequisites = [(1, 0), (3, 2)]  # Two separate chains
        self.assertTrue(can_finish_courses(num_courses, prerequisites))

if __name__ == '__main__':
    unittest.main()