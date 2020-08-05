class ComplexNumber:
    def __init__(self, first_number, second_number, *args):
        self.first_number = first_number
        self.second_number = second_number
        self.resilt = 'a + b * q'

    def __add__(self, other):
        print(f'Сумма чисел:')
        return f'resilt = {self.first_number + other.first_number} + {self.second_number + other.second_number} * q'

    def __mul__(self, other):
        print(f'Произведение чисел:')
        return f'resilt = {self.first_number * other.first_number - (self.second_number * other.second_number)} + {self.second_number * other.first_number} * q'

    def __str__(self):
        return f'resilt = {self.first_number} + {self.second_number} * q'


resilt_1 = ComplexNumber(-2, 3)
resilt_2 = ComplexNumber(3, 6)
print(resilt_1)
print(resilt_1 + resilt_2)
print(resilt_1 * resilt_2)