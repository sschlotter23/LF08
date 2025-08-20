def convert_num(number:int,base:int)->str:
    dez : int = 0
    result: str = ""
    if type(number) is not int or number < 0:
        raise Exception('number needs to be an positive integer')
    if type(base) is not int or base<1 or base>10:
        raise Exception('base needs to be an integer between 1 and 10')
    while dez >0:
        rest = dez % base
        result = str(rest) + result
        dez = int(dez / base)
    return result
   