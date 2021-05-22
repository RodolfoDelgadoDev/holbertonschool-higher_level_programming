#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' Test positives '''
    def positives(self):
        self.assertEqual([100, 101], 101)
        self.assertEqual([1], 1)
        self.assertEqual([0], 0)

    ''' Test negatives '''

    def negatives(self):
        self.assertEqual([-1, -2, -3], -1)
        self.assertEqual([1, 2, -1, 3], 3)
        self.assertEqual([-1, 0, -3, 5], 5)
