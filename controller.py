from model import Rectangle, Cube, Circle, Triangle, Pyramid, Shape2D, Shape3D
from view import FigureView

# класс для взаимодействия с фигурами
class FigureController:
    # инициализация создания объекта типа FigureView
    def __init__(self):
        self.view = FigureView()
    # функция для создания прямоугольника
    def create_rectangle(self, width, height):
        return Rectangle(width, height)
    # функция для создания круга
    def create_circle(self, radius):
        return Circle(radius)
    # функция для создания треугольника
    def create_triangle(self, a, h):
        return Triangle(a, h)
    # функция для создания пирамиды
    def create_pyramid(self, s, h):
        return Pyramid(s, h)
    # функция для создания куба
    def create_cube(self, a):
        return Cube(a)
    # функция для отображения информации о фигуре
    def display_figure_info(self, figure):
        # проверка на то принадлежит ли фигура классу Shape2D
        if isinstance(figure, Shape2D):
            self.view.display_square(figure)
        # проверка на то принадлежит ли фигура классу Shape3D
        elif isinstance(figure, Shape3D):
            self.view.display_volume(figure)
