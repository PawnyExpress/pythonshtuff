# Examples of conditional statemens and elif use for else if

#def evaluate_temp(temp):
    # Set an initial message
#    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
#    if temp > 38:
#        message = "Fever!"
#    return message

#def evaluate_temp_with_else(temp):
#    if temp > 38:
#        message = "Fever!"
#    else:
#        message = "Normal temperature."
#    return message

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

# write a function get_water_bill() that takes as input: num_gallons = the number of gallons of water that a customer used that month. 
# pricing structure <= 8000 is 5$ a month, <= 22000 is $6, <= 30k is $7 anything above $10 a month.

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = 5 * num_gallons / 1000
    elif num_gallons <= 22000:
        bill = 6 * num_gallons / 1000
    elif num_gallons <= 30000:
        bill = 7 * num_gallons / 1000
    else: 
        bill = 10 * num_gallons / 1000
    return bill