class Data:
    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)

    @classmethod
    def my_method(cls, day_month_year):
        my_list = []

        for i in day_month_year.split():
            if i != '-': my_list.append(i)

        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    @staticmethod
    def my_method_2(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return ':)'
                else:
                    return f'Неправильно введена дата!'


t = Data('12 - 1 - 2221')
print(t)
print(Data.my_method_2(11, 11, 2010))
print(Data.my_method('13 - 12 - 1999'))
print(t.my_method('11 - 11 - 2220'))
