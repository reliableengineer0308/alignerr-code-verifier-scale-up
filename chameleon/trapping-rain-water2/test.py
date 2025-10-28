import unittest
from solution import trap_rain_water

class TestTrappingRainWater(unittest.TestCase):
    
    def test_standard_case(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(trap_rain_water(height), 6)
    
    def test_deep_valley(self):
        height = [5, 2, 1, 0, 1, 2, 5, 1]
        self.assertEqual(trap_rain_water(height), 19)
    
    def test_multiple_peaks(self):
        height = [1, 3, 2, 5, 1, 4, 1, 2, 0, 3]
        self.assertEqual(trap_rain_water(height), 10)
    
    def test_stepped_structure(self):
        height = [3, 0, 2, 0, 4, 0, 1]
        self.assertEqual(trap_rain_water(height), 8)
    
    def test_no_trapping_increasing(self):
        height = [1, 2, 3, 4, 5]
        self.assertEqual(trap_rain_water(height), 0)
    
    def test_no_trapping_decreasing(self):
        height = [5, 4, 3, 2, 1]
        self.assertEqual(trap_rain_water(height), 0)
    
    def test_v_shaped(self):
        height = [5, 1, 5]
        self.assertEqual(trap_rain_water(height), 4)
    
    def test_u_shaped(self):
        height = [5, 1, 1, 1, 5]
        self.assertEqual(trap_rain_water(height), 12)
    
    def test_pyramid_shape(self):
        height = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(trap_rain_water(height), 0)
    
    def test_plateau(self):
        height = [2, 2, 2, 2, 2]
        self.assertEqual(trap_rain_water(height), 0)
    
    def test_single_tall_peak(self):
        height = [1, 1, 10, 1, 1]
        self.assertEqual(trap_rain_water(height), 0)
    
    def test_complex_mountain_range(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 2, 1, 0, 3]
        self.assertEqual(trap_rain_water(height), 20)
    
    def test_edge_cases(self):
        self.assertEqual(trap_rain_water([]), 0)
        self.assertEqual(trap_rain_water([5]), 0)
        self.assertEqual(trap_rain_water([1, 1, 1]), 0) 
        self.assertEqual(trap_rain_water([0, 0, 0, 0, 0]), 0)
    
    def test_maximum_constraints(self):
        height = [100000] * 100 
        self.assertEqual(trap_rain_water(height), 0)
        
        height = [0] * 100 
        self.assertEqual(trap_rain_water(height), 0)
    
    def test_alternating_peaks(self):
        height = [2, 0, 3, 0, 4, 0, 3, 0, 2]
        self.assertEqual(trap_rain_water(height), 10)
    
    def test_asymmetric_valley(self):
        height = [5, 0, 3, 0, 2, 0, 4]
        self.assertEqual(trap_rain_water(height), 15)
    
    def test_wave_pattern(self):
        height = [2, 1, 3, 1, 4, 1, 3, 1, 2]
        self.assertEqual(trap_rain_water(height), 6)

if __name__ == '__main__':
    unittest.main()