def type_logger(func):
    def wrapper(*args):
        endof = "\n"
        if len(args) > 1:
            endof = ","
        for arg in args:
            print(f"{func.__name__}({arg}: {type(arg)})", end=endof)
        result = func(*args)
        return result
    return wrapper


@type_logger
def calc_cube(*x):
    y = []
    for x_current in x:
        y.append(x_current**3)
    return y


calc_cube(5, 6)
