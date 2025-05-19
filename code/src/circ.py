import numpy as np

class circ:
    """
    A class to handle circular objects in the simulation.
    """

    def __init__(self, x, y, r, dphi):
        """
        Initialize the Circle class.
        """
        self.x = x  # x-coordinate of the center
        self.y = y  # y-coordinate of the center
        self.r = r  # radius of the circle
        self.dphi = dphi  #part of the angle thats simulated, for example 0.1*2*np.pi for 10% of the circle

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