import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
	def testAccurateDiscount(self):
	#test 1 --> verify right values are returned for normal cases
	discount_price = calculate_discount	(100, 10, 30)

	self.assertEqual(discount_price, 60)

#case 1 --> final cost should never go below zero

#case 2 --> discounts can never be greater than 