def calculate_discount(item_cost, relative_discount, absolute_discount):
	item_cost = item_cost * 1.0
	relative_discount = relative_discount / 100.0
	absolute_discount = absolute_discount

	item_cost = item_cost * (1 - relative_discount)
	item_cost = item_cost - absolute_discount

	return item_cost

def main():
	item_cost = calculate_discount(100, 10, 30)
	print item_cost

if __name__ == "__main__":
	main()
