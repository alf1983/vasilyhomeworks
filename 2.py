class MyExceptionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Введите делимое: ")
try:
    dividend = int(dividend)
except ValueError:
    print("Делимое должно быть числом")
    exit(0)
divider = input("Введите делитель: ")
try:
    divider = int(divider)
    if divider == 0:
        raise MyExceptionByZero("На нуль делить нельзя!")
except ValueError:
    print("Делитель должен быть числом")
    exit(0)
except MyExceptionByZero as error:
    print(error)
else:
    print(f"{dividend} : {divider} = {dividend / divider}")
