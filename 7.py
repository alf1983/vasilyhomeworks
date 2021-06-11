class ComplexNumbers:
    def __init__(self, complex_number):
        self.complex_number = self.valid_complex_number(complex_number)
        if self.complex_number is False:
            exit(0)

    @staticmethod
    def valid_complex_number(complex_number):
        complex_number = complex_number.replace(" ", "").replace("i", "j")
        try:
            result = complex(complex_number)
        except ValueError:
            print(f"{complex_number} is not complex_number")
            return False
        return result

    def __add__(self, other):
        real = str(self.complex_number.real + other.complex_number.real)
        imag = str(self.complex_number.imag + other.complex_number.imag) + "j"
        return complex(real+"+"+imag)

    def __mul__(self, other):
        sign = "+"
        real = str((self.complex_number.real * other.complex_number.real)
                   - (self.complex_number.imag * other.complex_number.imag))
        imag = (self.complex_number.imag * other.complex_number.real) + (self.complex_number.real * other.complex_number
                                                                         .imag)
        if imag < 0:
            sign = ""
            imag = str(imag)+"j"
        return complex(real+sign+imag)


a = ComplexNumbers("3+5j")
b = ComplexNumbers("-4+2j")
c = 3+5j
d = -4+2j
print(a+b)
print(c+d)
print(a*b)
print(c*d)

