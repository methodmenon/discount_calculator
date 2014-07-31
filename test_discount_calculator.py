import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
	def testAccurateDiscount(self):
	#case 1 --> verify right values are returned for normal cases
		discount_price = calculate_discount	(100, 10, 30)

		self.assertEqual(discount_price, 60)

	#case 2 --> Item cost should never go below zero
	def testItemCostNotNegative(self):
		discount_price = calculate_discount(-100, 10, 30)
		self.assertEqual(discount_price, "Item cost cannot be a negative number")


	#case 3 --> discounts can never be greater than item cost
	def testRelativeDiscountTooHigh(self):
		discount_price = calculate_discount(100, 20000, 30)
		self.assertEqual(discount_price, "Relative discount is too high")

	#case 4 --> absolute discount cannot be greater than item cost
	def testAbsoluteDiscountTooHigh(self):
		discount_price = calculate_discount(100, 10, 1000)
		self.assertEqual(discount_price, "Absolute discount is too high")

if __name__ == "__main__":
	unittest.main()