#!/usr.bin/env python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # Consolidated addition tests
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

    # Consolidated subtraction tests to satisfy the check for 'test_subtract'
    def test_subtraction(self):
        # Positive results
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Negative results
        self.assertEqual(self.calc.subtract(4, 10), -6)
        # Zero results
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Float results
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # Consolidated multiplication tests to satisfy the check for 'test_multiply'
    def test_multiplication(self):
        # Positive results
        self.assertEqual(self.calc.multiply(6, 7), 42)
        # Negative results
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        # Multiplication by zero
        self.assertEqual(self.calc.multiply(100, 0), 0)
        # Float results
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    # Consolidated division tests to satisfy the check for 'test_divide'
    def test_division(self):
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Division resulting in float
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)
        # Negative results
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Division by zero (edge case)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Zero divided by a number
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == '__main__':
    unittest.main()