import numpy as np
import matplotlib.pyplot as plt
class circ:
    """
    A class to handle circular objects in the simulation.
    """

    def __init__(self, x, y, r, dphi, rot=0):
        """
        Initialize the Circle class.
        """
        self.x = x  # x-coordinate of the center
        self.y = y  # y-coordinate of the center
        self.r = r  # radius of the circle
        self.dphi = dphi  #part of the angle thats simulated, for example 0.1*2*np.pi for 10% of the circle
        self.rot = rot

    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
    def get_r(self):
        return self.r

    def get_normal(self, x, y):
        """
        Calculate the normal vector at a point on the circle.
        """
        # Normalize the vector from the center to the point
        norm = np.array([x - self.x, y - self.y])
        norm /= np.linalg.norm(norm)
        return norm

    def get_points(self, dx):
        """
        Get the points of the circle.
        """
        phi = np.arange(0, self.dphi, dx)  # Generate angles from 0 to dphi
        x_vals = self.x + self.r * np.cos(phi + self.rot)
        y_vals = self.y + self.r * np.sin(phi + self.rot)
        return x_vals, y_vals

    def print(self, c):
        """
        Plot the circle (or part of it) with the specified color.
        """
        phi = np.linspace(0, self.dphi, 100)  # Generate angles from 0 to dphi
        x_vals = self.x + self.r * np.cos(phi + self.rot)  # x-coordinates
        y_vals = self.y + self.r * np.sin(phi + self.rot)  # y-coordinates
        plt.plot(x_vals, y_vals, color=c)