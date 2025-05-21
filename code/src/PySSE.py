#contains the PySSE class
import numpy as np
import matplotlib.pyplot as plt


class PySSe:
    """
    A class to handle PySSE (Python for Speaker Simulations Enviroment) library.
    """

    def __init__(self):
        """
        Initialize the PySSE class.
        """
        plt.axis('equal')
        self.x=100   #xsize of container
        self.y=100   #ysize of container
        self.dx=0.1  #resolution of grid
        self.v_sound = 343  #speed of sound m/s
        self.steps = 100  #number of time steps
        #self.dt=0  #time step
        self.dt = self.dx/(np.sqrt(2) * self.v_sound)  # CFL-Bedingung
        self.objects = []  #list of objects in the container
        pass

    #write getters and setters for all attributes
    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_dx(self):
        return self.dx

    def set_dx(self, dx):
        self.dx = dx

    def get_v_sound(self):
        return self.v_sound

    def set_v_sound(self, v_sound):
        self.v_sound = v_sound

    def get_steps(self):
        return self.steps

    def set_steps(self, steps):
        self.steps = steps

    def get_dt(self):
        return self.dt

    def set_dt(self, dt):
        self.dt = dt


    def add_obj(self, obj):
        #adds an object to the container
        self.objects.append(obj)

    def print(self):
        #prints the objects in the container
        for obj in self.objects:
            obj.print('blue')
        plt.show()


    def run_sim(self):
        #runs the simulation in respect to all lines
        return