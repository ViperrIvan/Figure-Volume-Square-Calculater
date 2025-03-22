import abc

# абстактный класс для наследования от него классов Shape2D и Shape3D
class Figure(abc.ABC):
    pass

# абстрактный класс для наследования от него 2D фигур
class Shape2D(Figure):
    @abc.abstractmethod
    def square(self): pass

# абстрактный класс для наследования от него 3D фигур
class Shape3D(Figure):
    @abc.abstractmethod
    def volume(self): pass

# класс треугальника
class Rectangle(Shape2D):
    # инициализация высоты и ширины прямоугольника
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # функция для вычисления площади прямоугольника
    def square(self): return self.width * self.height

# класс круга
class Circle(Shape2D):
    # инициализация радиуса круга
    def __init__(self, radius):
        self.radius = radius
    # функция вычисления площади круга
    def square(self): return self.radius * self.radius * 3.14

# класс треугольника
class Triangle(Shape2D):
    # инициализация высоты и ширины треугольника
    def __init__(self, a, h):
        self.a = a
        self.h = h
    # функция вычисления площади треугольника
    def square(self): return self.a * self.h / 2

# класс пирамиды
class Pyramid(Shape3D):
    # инициализация площади основания и высоты пирамиды
    def __init__(self, s, h):
        self.h = h
        self.s = s
    # функция вычисления объема пирамиды
    def volume(self): return 1/3 * self.s * self.h

# класс куба
class Cube(Shape3D):
    # инициализация длинны строны куба
    def __init__(self, a):
        self.a = a
    # функция вычисления объема куба
    def volume(self): return self.a * self.a * self.a
