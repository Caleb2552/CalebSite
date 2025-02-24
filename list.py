def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return "num_of_days  " + str(num_of_days * 24) + " hours"
    elif conversion_unit == "minutes":
        return "num_of_days  " + str(num_of_days * 24 * 60) + " minutes" 
    else:
        return "unsupported unit"      

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])


        # conversion only for positive integers.....
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, pls enter a valid positive number!")
        else:
            print("you entered a negative, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")


user_input_message = "Hey user, enter number of days and conversion unit!\n"        
