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