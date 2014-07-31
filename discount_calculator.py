def calculate_discount(item_cost, relative_discount, absolute_discount):
	while (item_cost >= 0):
		item_cost = item_cost * 1.0
		relative_discount = relative_discount / 100.0
		if (relative_discount > item_cost):
			return"Relative discount is too high"
		else:
			absolute_discount = absolute_discount
			item_cost = item_cost * (1 - relative_discount)
			if (absolute_discount > item_cost):
				return "Absolute discount is too high"
			else:
				item_cost = item_cost - absolute_discount
				return item_cost
	else:
		return "Item cost cannot be a negative number"

def main():
	"""
	Verifying that the function works
	"""
	item_cost = calculate_discount(100, 10, 30)
	print item_cost

	item_cost = calculate_discount(-100, 10, 30)
	print item_cost

	item_cost = calculate_discount(100, 20000, 30)
	print item_cost

	item_cost = calculate_discount(100, 10, 1000)
	print item_cost

if __name__ == "__main__":
	main()
