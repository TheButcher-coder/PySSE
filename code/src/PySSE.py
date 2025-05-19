#contains the PySSE class
import numpy as np

class PySSe:
    """
    A class to handle PySSE (Python for Speaker Simulations Enviroment) library.
    """

    def __init__(self):
        """
        Initialize the PySSE class.
        """
        self.x=100   #xsize of container
        self.y=100   #ysize of container
        self.dx=0.1  #resolution of grid
        self.v_sound = 343  #speed of sound m/s
        self.steps = 100  #number of time steps
        #self.dt=0  #time step
        self.dt = self.dx/(np.sqrt(2) * self.v_sound)  # CFL-Bedingung

        pass

    def example_method(self):
        """
        An example method that does nothing.
        """
        pass