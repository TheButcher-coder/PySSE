#contains the PySSE class
from . import Line
from . import circ
from . import rec
from . import Mic as Mic

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
        self.dt = self.dx / (np.sqrt(2) * self.v_sound)  # CFL-Bedingung

    def get_v_sound(self):
        return self.v_sound

    def set_v_sound(self, v_sound):
        self.v_sound = v_sound
        self.dt = self.dx / (np.sqrt(2) * self.v_sound)  # CFL-Bedingung

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
            obj.print('blue', self.dx)
        #plt.show()

    def get_angle(self, v1, v2):
        return np.arccos(v1@v2/(np.linalg.norm(v1)*np.linalg.norm(v2)))

    def does_collide(self, x, y):
        #checks if the point x,y is on a line
        #returns true if it is on a line

        for obj in self.objects:
            x_obj, y_obj = obj.get_points(self.dx)
            for i in range(len(x_obj)):
                if x_obj[i] == x and y_obj[i] == y:
                    return obj
        return None

    def mirror_point(self, v, p, n):
        '''
        Mirrors the vector at the point p1 at the line defined by p2 and n.
        :param v: vector
        :param p: base point of vector
        :param n: second vector
        :return:
        '''
        alpha = self.get_angle(v, n)
        T = np.array([[np.cos(alpha), -np.sin(alpha), p[0]],
                      [np.sin(alpha), np.cos(alpha), p[1]],
                      [0, 0, 1]])
        v_m = T @ np.array([v[0], v[1], 1])
        v_m[1] = -v_m[1]
        return np.linalg.inv(T)@v_m     #transform back to global system and return

    def run_sim(self):
        # Korrekte Gitterdimensionen berechnen
        nx = int(self.x / self.dx)
        ny = int(self.y / self.dx)

        # Maske für solide Objekte erstellen
        solid_mask = np.zeros((nx, ny), dtype=bool)
        for obj in self.objects:
            obj_mask = obj.get_mask(nx, ny, self.dx)
            solid_mask = np.logical_or(solid_mask, obj_mask)

        # Druckfelder initialisieren
        p = np.zeros((nx, ny))
        p_old = np.zeros((nx, ny))
        p_new = np.zeros((nx, ny))

        # Position der Quelle
        i_source = nx // 2
        j_source = ny // 2

        # Quelle darf nicht in solidem Objekt sein
        if solid_mask[i_source, j_source]:
            raise ValueError("Quelle befindet sich in einem Objekt!")

        for t in range(self.steps):
            for i in range(1, nx - 1):
                for j in range(1, ny - 1):
                    # Wellengleichung lösen
                    laplacian = (p[i + 1, j] + p[i - 1, j] +
                                 p[i, j + 1] + p[i, j - 1] -
                                 4 * p[i, j]) / self.dx ** 2
                    p_new[i, j] = (2 * p[i, j] - p_old[i, j] +
                                   self.v_sound ** 2 * self.dt ** 2 * laplacian)

            # Quelle anregen (nur in den ersten 5 Schritten)
            if t < 5:
                p_new[i_source, j_source] += np.sin(2 * np.pi * 500 * self.dt * t)

            # Druck in soliden Bereichen auf Null setzen
            p_new[solid_mask] = 0

            # Felder aktualisieren
            p_old, p = p, p_new.copy()

            # Visualisierung
            if t % 5 == 0:
                plt.cla()
                plt.imshow(p.T, cmap='RdBu', vmin=-0.01, vmax=0.01, origin='lower')
                plt.title(f"t = {t}")
                plt.plot(self.mic.get_x(), self.mic.get_y(), 'ro')  # Plot microphone position
                self.print()

                plt.pause(0.01)

            self.mic.add_data(p[self.mic.get_x(), self.mic.get_y()])

        plt.show()
        return

    def add_mic(self, x, y):
        self.mic = Mic.Mic(x, y)

    def plot_mic_data(self):
        """
        Plot the data collected by the microphone.
        """
        if hasattr(self, 'mic'):
            self.mic.plot_data()
        else:
            print("No microphone data to plot.")