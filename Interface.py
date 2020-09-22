# Класс интерфейса
class Interface:
    # Конструктор
    def __init__(self):
        pass
    # Главное меню:
    def Interface_Main(self):
        print ("Главное меню:")
        print ("Выберите действие:")
        print ("1 - Ввести бинарное дерево.")
        print ("2 - Вывести бинарное дерево.")
        print ("3 - Заменить все вершины дерева на их абсолютные величины.")
        print ("4 - Определить максимальную глубину дерева.")
        print ("5 - Выход из программы.")
        pass

    # Защита от некорректного ввода:
    def input_Controller(self):
        while True:
            try:
                Value = int(input(">>> "))
                if Value > 0:
                    return Value
                else:
                    print("Ошибка ввода!")
            except ValueError:
                print("Ошибка ввода!")
                print("")

    # Защита от некорректного ввода:
    def input_Controller2(self):
        while True:
            try:
                Value = float(input(">>> "))
                return Value
            except ValueError:
                print("Ошибка ввода!")
                print("")