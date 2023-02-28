
def add_zeros(number_string):
    """This takes in a number string of any format and returns the number back in the correct format
    for working with it numerically. The string "40" becomes the number 40000"""

    # Try to run the function on the number string
    try:

        # If the number has a period in it then it needs to be treated as a float
        if '.' in number_string:

            # We split the number string on the period
            split_number_string = number_string.split('.')

            # We then look at the length of the final string representing the
            # decimal part of the number
            # If the length is 1 we need to add 
            if len(split_number_string[1]) == 1:
                split_number_string[1] = split_number_string[1] + '00'
            elif len(split_number_string[1]) == 2:
                split_number_string[1] = split_number_string[1] + '0'
            number_string = split_number_string[0] + split_number_string[1]
            number = int(number_string)

        elif len(number_string) == 1 or len(number_string) == 2 or len(number_string) == 3:
            number = int(number_string) * 1000
        else:
            number = int(number_string)
        return number

    # Raise a value error if an incorrect value is inputted
    except ValueError as e:
        print("You tried to input an invalid value to this function")
        print(e)


add_zeros('')




