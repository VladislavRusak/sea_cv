import unittest
from src.cv.angle_calculation import calculate_angle

class TestAngleCalculation(unittest.TestCase):

    def test_angle_calculation_valid(self):
        # Example frame data for testing
        frame_data = ...  # Replace with actual frame data or mock
        expected_angle = ...  # Replace with expected angle based on frame data
        
        calculated_angle = calculate_angle(frame_data)
        self.assertAlmostEqual(calculated_angle, expected_angle, places=2)

    def test_angle_calculation_invalid(self):
        frame_data = None  # Invalid input
        with self.assertRaises(ValueError):
            calculate_angle(frame_data)

if __name__ == '__main__':
    unittest.main()