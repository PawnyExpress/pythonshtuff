
#small calculator used to calculate the cost of painting walls and ceilings, calculates the amount of gallons for one layer of paint.
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
    
    
    project_cost = get_cost(585, 215, 350, 19)
    
    return cost