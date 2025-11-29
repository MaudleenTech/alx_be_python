#!/usr.bin/env python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # Consolidated addition tests to satisfy the check for 'test_addition'
    def test_addition(self):
        # Positive numbers
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(100, 200), 300)
        # Negative numbers
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(-10, -5), -15)
        # Floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_float_result(self):
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)
        
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        
    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == '__main__':
    unittest.main()