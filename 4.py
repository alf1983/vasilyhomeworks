def val_checker(is_valid):
    def wrapper(func):
        def validator_ex(*args):
            if is_valid(*args):
                return func(*args)
            else:
                raise ValueError(f'wrong value {args}')
        return validator_ex
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3


print(calc_cube(0))
