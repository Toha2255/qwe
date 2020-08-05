class Store:

    def __init__(self, name, quantity, price, numberList, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numberList = numberList
        self.my_store_full = []
        self.my_store = []
        self.user = {f'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.user.update(unique)
            self.my_store.append(self.user)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numberList} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numberList} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numberList} times'


first = Printer('hp', 900, 2, 13)
second = Scanner('Canon', 7000, 79, 15)
three = Copier('Xerox', 15000, 1, 11)
print(first.reception())
print(second.reception())
print(three.reception())
print(first.to_print())
print(three.to_copier())
