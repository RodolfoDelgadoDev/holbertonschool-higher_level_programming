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

    ''' Test Task 1 '''

    def test_BaseNone(self):
        ''' test '''
        b = Base(None)
        self.assertEqual(b.id, 1)

    ''' Test Task 1 '''

    def test_BaseNegative(self):
        ''' test '''
        b = Base(-3)
        self.assertEqual(b.id, -3)

    ''' Test Task 1 '''

    def test_BaseEmpty(self):
        ''' test '''
        b = Base()
        self.assertEqual(b.id, 1)

if __name__ == '__main__':
    unittest.main()
