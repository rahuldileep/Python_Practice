#!/usr/bin/env python3 

import unittest
from name_format import rearrange

class TestRearrange(unittest.TestCase):
	def test_basic(self):
		testcase = "Jadhav, Rahul"
		expected = "Rahul Jadhav"
		self.assertEqual(rearrange(testcase),expected)

	def test_onename(self):
		testcase = "Rahul"
		expected = "Rahul"
		self.assertEqual(rearrange(testcase),expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange(testcase),expected)

	def test_with_initials(self):
		testcase = "Jadhav, Rahul D."
		expected = "Rahul D. Jadhav"
		self.assertEqual(rearrange(testcase),expected)

unittest.main()
