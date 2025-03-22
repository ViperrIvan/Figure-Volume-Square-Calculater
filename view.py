# класс для отображения вывода фигур
class FigureView:
    # статический метод для вывода площади фигуры
    @staticmethod
    def display_square(figure):
        print(f"Square of {figure.__class__.__name__}: {figure.square()}")
    # статический метод для вывода объема фигуры
    @staticmethod
    def display_volume(figure):
        print(f"Volume of {figure.__class__.__name__}: {figure.volume()}")
