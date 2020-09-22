# Список импортов
from Binary_Tree import Binary_Tree
from Interface import Interface

# Консольное меню программы
Menu = Interface()
# Вызов метода отображения главного меню
Menu.Interface_Main()
# Создание объекта класса Дерево
tree = Binary_Tree()
# Строка вывода
output_string = ""

# Цикл обработки команд
while True:
    # Ввод выбранного действия
    Step = Menu.input_Controller()

    # Ввод дерева
    if Step == 1:
        print("")
        print("Введите количество элементов дерева: ")
        tree.root = None
        length = Menu.input_Controller()
        print("Последовательно введите элементы дерева:")
        for i in range(length):
            value = Menu.input_Controller2()
            tree.root = tree.tree_recursive_Creation(tree.root, value)
        print("Произвольное бинарное дерево было успешно рекурсивно создано")
        print("")
        Menu.Interface_Main()

    # Вывод дерева
    elif Step == 2:
        print("")
        output_string = tree.tree_Output(tree.root)
        if output_string is "":
            print("Исходное дерево пустое")
            print("")
        else:
            print("Введенное произвольное бинарное дерево:")
            print(output_string)
            print("")
        Menu.Interface_Main()

    # Замена на абсолютные величины
    elif Step == 3:
        if tree.root is not None:
            print("")
            print("Дерево после замены всех вершин на их абсолютные величины:")
            tree.root = tree.abs_Replace(tree.root)
            print(tree.tree_Output(tree.root))
            print("")
        else:
            print("Исходное дерево пустое")
            print("")
        Menu.Interface_Main()

    # Определение максимальной глубины
    elif Step == 4:
        print("")
        print("Глубина введенного дерева:")
        print(tree.max_Depth(tree.root, 0))
        print("")
        Menu.Interface_Main()

    # Выход из программы
    elif Step == 5:
        print("Программа завершена")
        break

    # Остальные случаи
    else:
        print("Ошибка ввода")
        print("")



