#!/usr/bin/python3

################################
# File Name:	Alexandrea Beh
# Date:			11/19/2014
# Class:		CS 360
# Assignment:	Willamette
# Purpose:		Unittest for Basket
################################

import unittest
from basket import Basket

class TestBasket(unittest.TestCase):
	def setUp(self):
		""" necessary setup for the tests to run
		"""
		self.__init__
		
	def test_AddItem(self):
		""" test that an item actually gets added to the basket
		"""
		item = SaleItem (['10', '2', 'ATestItem'])
		self.addItem (1, item)
		
		testID = item[1].getID()
		
		self.assertEqual(self.contains(testID), True)

		
