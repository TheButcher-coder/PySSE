#contains line objects for reflections
import numpy as np
import matplotlib.pyplot as plt
class Line:
    """
    A class to handle lines in the simulation.
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initialize the Line class.
        """
        self.x1 = x1  # x-coordinate of the first point
        self.y1 = y1  # y-coordinate of the first point
        self.x2 = x2  # x-coordinate of the second point
        self.y2 = y2  # y-coordinate of the second point

    def get_x1(self):
        return self.x1
    def set_x1(self, x1):
        self.x1 = x1
    def get_y1(self):
        return self.y1
    def set_y1(self, y1):
        self.y1 = y1
    def get_x2(self):
        return self.x2
    def set_x2(self, x2):
        self.x2 = x2
    def get_y2(self):
        return self.y2

    def get_normal(self):
        """
        Calculate the normal vector of the line.
        """
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        length = np.sqrt(dx**2 + dy**2)
        return np.array([-dy / length, dx / length])

    def get_points(self, dx):
        """
        Get the points of the line.
        """
        if self.x1 < self.x2:
            x_vals = np.arange(self.x1, self.x2, dx)
        else:
            x_vals = np.flip(np.arange(self.x2, self.x1, dx))

        if self.y1 < self.y2:
            y_vals = np.arange(self.y1, self.y2, dx)
        else:
            y_vals = np.flip(np.arange(self.y2, self.y1, dx))

        return x_vals, y_vals


    def print(self, c, dx):
        """
        Plot the line from point 1 to point 2 with the specified color.
        """
        plt.plot([self.x1/dx, self.x2/dx], [self.y1/dx, self.y2/dx], color=c)

    def get_mask(self, nx, ny, dx):
        mask = np.zeros((nx, ny), dtype=bool)
        x_points, y_points = self.get_points(dx)
        #print((zip(x_points, y_points)))
        for x, y in zip(x_points, y_points):
            i = int(x / dx)
            j = int(y / dx)
            if 0 <= i < nx and 0 <= j < ny:
                mask[i, j] = True
        return mask