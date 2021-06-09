#!/usr/bin/python3
"""Unittest for base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' Test Task 1 '''

    def test_BaseT1(self):
        ''' test '''
        b = Base(3)
        self.assertEqual(b.id, 3)
        b = Base(None)
        self.assertEqual(b.id, 1)
        b = Base(-3)
        self.assertEqual(b.id, -3)
        b = Base()
        self.assertEqual(b.id, 2)

if __name__ == '__main__':
    unittest.main()
