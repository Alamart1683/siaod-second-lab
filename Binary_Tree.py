# Импорт класса узла бинарного дерева
from Binary_Tree_Node import Binary_Tree_Node

# Класс бинарного дерева
class Binary_Tree(object):
    # Конструктор
    def __init__(self):
        self.root = None

    # Метод рекурсивного создания произвольного бинарного дерева из строки
    def tree_recursive_Creation(self, current_node, data):
        # Проверка на пустоту
        if current_node is None:
            return Binary_Tree_Node(data)
        if data < current_node.data:
            current_node.left = self.tree_recursive_Creation(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self.tree_recursive_Creation(current_node.right, data)
        return current_node

    # Метод рекурсивного вывода дерева
    def tree_Output(self, current_node):
        # Проверка на пустоту
        if current_node is None:
            return ""
        if current_node.left is None and current_node.right is None:
            return str(current_node.data) + ""
        if current_node.right is None:
            return str(current_node.data) + "(" + self.tree_Output(current_node.left) + ")"
        #if current_node.left is None:
            #return str(current_node.data) + "(" + self.tree_Output(current_node.right) + ")"
        return str(current_node.data) + "(" + self.tree_Output(current_node.left) + ")(" + self.tree_Output(current_node.right) + ")"

    # Метод замены отрицательных узлов их абсолютными величинами
    def abs_Replace(self, current_node):
        # Проверка на пустоту
        if self.root != None:
            # Обход левого поддрева
            if current_node.left is not None:
                self.abs_Replace(current_node.left)
            if current_node.data < 0:
                current_node.data = abs(current_node.data)
            # Обход правого поддрева
            if current_node.right is not None:
                self.abs_Replace(current_node.right)
            return current_node

    # Метод определения максимальной глубины дерева
    def max_Depth(self, current_node, depth):
        if current_node is None:
            return depth
        return max(self.max_Depth(current_node.left, depth + 1), self.max_Depth(current_node.right, depth + 1))