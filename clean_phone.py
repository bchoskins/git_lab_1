import pandas as pd 

def validate_phone(phone_number):
    """ Ensure that phone numbers are in a valid format

    Keyword arguments:
    phone_number -- A Pandas Series of phone_numbers as strings
    
    Returns: A boolean Pandas Series. Valid phone numbers are True. Invalid are False.
    """
    bool_phone = phone_number.str.contains("^\d{3}[-]?\d{3}[-]?\d{4}")
    return bool_phone

numbers = pd.Series(['574-252-6163', '2242344039', 'bad 312-252-6265'])
print(validate_phone(numbers))