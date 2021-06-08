#!/usr/bin/python3
"""Unittest for base
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    ''' Test Task 1 '''
    def test_BaseT0(self):
        ''' test '''
        b = Base(3)
        self.assertEqual(b.id, 3)
        b = Base(100)
        self.assertEqual(b.id, 100)
        b = Base(None)
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base(-3)
        self.assertEqual(b.id, -3)
        b = Base()
        self.assertEqual(b.id, 4)

if __name__ == '__main__':
    unittest.main()
