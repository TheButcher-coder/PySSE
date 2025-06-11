import numpy as np
from . import Line as line

class rec:
    """
    A class to handle rectangular objects in the simulation.
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initialize the Rectangle class.
        """
        #do it with lines instead
        self.lines = []
        self.lines.append(line.Line(x1, y1, x2, y1))
        self.lines.append(line.Line(x2, y1, x2, y2))
        self.lines.append(line.Line(x2, y2, x1, y2))
        self.lines.append(line.Line(x1, y2, x1, y1))

    def get_lines(self):
        return self.lines

    def get_points(self, dx):
        """
        Get the points of the rectangle.
        """
        x, y = [], []
        for l in self.lines:
            x_vals, y_vals = l.get_points(dx)
            x.append(x_vals)
            y.append(y_vals)
        return x, y
    def print(self, c):
        """
        Plot the rectangle with the specified color.
        """
        for line in self.lines:
            line.print(c)

    def get_mask(self, nx, ny, dx):
        x_coords = np.arange(nx) * dx
        y_coords = np.arange(ny) * dx
        X, Y = np.meshgrid(x_coords, y_coords, indexing='ij')
        return (X >= self.x) & (X <= self.x + self.w) & \
            (Y >= self.y) & (Y <= self.y + self.h)