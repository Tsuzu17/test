def add_it(a,b,c,d=10,e=20):
      """ Returns the result of two optional params
    multiplied by the addition of 3 required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return: int.
    """
    return (a + b + c)*d/e

result = add_it(30,40,50)
print(result)
