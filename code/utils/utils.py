def convert_currency(currency_str):
    """
    Convert a currency string to a float.

    :param currency_str: Currency string (e.g., '1 234,56 €')
    :return: Float representation of the currency
    """
    return float(currency_str.replace('\xa0', '').replace(',', '.').strip('€').strip())

def convert_area(area_str):
    """
    Convert an area string to a float.

    :param area_str: Area string (e.g., '123,45 m²')
    :return: Float representation of the area
    """
    return float(area_str.split(" ")[0].replace(',', '.'))

def convert_fee(price_str):
    """
    Convert a fee string to a float.

    :param price_str: Fee string (e.g., '123,45 €/m²')
    :return: Float representation of the fee
    """
    cleaned_price_str = price_str.split(" ")[0].replace("\xa0", "").replace("€", "").replace(",", ".")
    return float(cleaned_price_str)

def convert_to_int(string):
    """
    Extract and convert all digits in a string to an integer.

    :param string: String containing digits
    :return: Integer representation of the digits
    """
    return int(''.join(filter(str.isdigit, string)))