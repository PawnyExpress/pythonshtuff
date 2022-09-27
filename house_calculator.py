
#calculator for cost of a home and checking if it has a basement or not.
# the expected cost for a house with 0 bedrooms and 0 bathrooms, and no basement is 80000,
# each bedroom adds 30000 to the expected cost,
# each bathroom adds 10000 to the expected cost, and
# a basement adds 40000 to the expected cost

def get_expected_cost(beds, baths, has_basement):
    value = 80000 + beds * 30000 + baths * 10000 + has_basement * 40000
    return value