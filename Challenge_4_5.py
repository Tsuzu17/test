def con(string):
    """ Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c =con("105.5")
print(c)
