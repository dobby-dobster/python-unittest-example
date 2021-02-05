#!/usr/bin/env python

import unittest
import main

class AddTest(unittest.TestCase):
    def test(self):
        self.assertEqual(main.add(3, 4), 7)

class MultipleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(main.multiple(3, 3), 9)

class IsTrueTest(unittest.TestCase):
    def test(self):
        var = False
        self.assertTrue(main.istrue(var))

if __name__ == '__main__':
    unittest.main()