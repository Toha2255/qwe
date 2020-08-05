class Prog(Exception):
    def __init__(self, *args):
        self.my_lyst = []

    def my(self):
        while True:
            try:
                q = int(input('chislo '))
                self.my_lyst.append(q)
                print(self.my_lyst)

            except:
                print("eror ")
                a = input("Желаете продолжить? Если нет, нажмите - Q. ")
                if a == "Q":
                    print(self.my_lyst)
                    break



e = Prog()
print(e.my())
