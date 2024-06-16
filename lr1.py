import tkinter as tk
import copy
from abc import ABC, abstractmethod

# Абстрактный класс для фигуры
class Shape(ABC):
    @abstractmethod
    def draw(self, canvas, x, y):
        pass

    @abstractmethod
    def clone(self):
        pass

# Класс для круга
class Circle(Shape):
    def draw(self, canvas, x, y):
        radius = 30
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline='black', fill='blue')

    def clone(self):
        return copy.deepcopy(self)

# Класс для треугольника
class Triangle(Shape):
    def draw(self, canvas, x, y):
        size = 50
        points = [x, y - size, x - size, y + size, x + size, y + size]
        canvas.create_polygon(points, outline='black', fill='red')

    def clone(self):
        return copy.deepcopy(self)

# Класс для прямоугольника
class Rectangle(Shape):
    def draw(self, canvas, x, y):
        width = 60
        height = 40
        canvas.create_rectangle(x - width/2, y - height/2, x + width/2, y + height/2, outline='black', fill='green')

    def clone(self):
        return copy.deepcopy(self)

# Основной класс приложения
class ShapeApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()

        self.shapes = {
            'Circle': Circle(),
            'Triangle': Triangle(),
            'Rectangle': Rectangle()
        }

        self.selected_shape = None

        self.create_ui()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        self.shape_var = tk.StringVar(value='Circle')

        for shape_name in self.shapes.keys():
            rb = tk.Radiobutton(frame, text=shape_name, variable=self.shape_var, value=shape_name, command=self.on_shape_select)
            rb.pack(side=tk.LEFT)

    def on_shape_select(self):
        shape_name = self.shape_var.get()
        self.selected_shape = self.shapes[shape_name].clone()

    def on_canvas_click(self, event):
        if self.selected_shape:
            self.selected_shape.draw(self.canvas, event.x, event.y)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()
