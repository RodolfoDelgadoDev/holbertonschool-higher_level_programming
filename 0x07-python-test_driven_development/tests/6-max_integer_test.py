#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' Test positives '''
    def test_positives(self):
        self.assertEqual(max_integer([100, 101]), 101)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), None)
    ''' Test negatives '''

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, -1, 3]), 3)
        self.assertEqual(max_integer([-1, 0, -3, 5]), 5)

if __name__ == '__main__':
    unittest.main()
