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

    def print(self, c):
        """
        Plot the rectangle with the specified color.
        """
        for line in self.lines:
            line.print(c)