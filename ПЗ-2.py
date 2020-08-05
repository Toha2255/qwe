class Number:
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber


class Division(Exception):
    def devesion_null(self, firstNumber, secondNumber):
        try:
            return (firstNumber / secondNumber)
        except ZeroDivisionError:
            return f'Деление на 0 запрещено!'


d = Division(12, 10)
print(d.devesion_null(12, 0))
print(d.devesion_null(12, 2))
