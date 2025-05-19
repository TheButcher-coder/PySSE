import numpy as np
import lines as l

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
        self.lines.append(l.Line(x1, y1, x2, y1))
        self.lines.append(l.Line(x2, y1, x2, y2))
        self.lines.append(l.Line(x2, y2, x1, y2))
        self.lines.append(l.Line(x1, y2, x1, y1))

    def __init__(self, l1, l2, l3, l4):
        """
        Initialize the Rectangle class.
        """
        #do it with lines instead
        self.lines = []
        self.lines.append(l1)
        self.lines.append(l2)
        self.lines.append(l3)
        self.lines.append(l4)

    def get_lines(self):
        return self.lines