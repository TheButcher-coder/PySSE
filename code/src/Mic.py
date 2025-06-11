import numpy as np
import matplotlib.pyplot as plt



class Mic:
    '''Class for a microphone in the PySSE simulation.'''
    def __init__(self, x, y):
        """
        Initialize the microphone with position (x, y) and radius.
        """
        self.x = x
        self.y = y
        self.data = np.array([])

    #make all getters and setters
    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_data(self):
        return self.data

    def add_data(self, new_data):
        """Append new data to the microphone's data array."""
        self.data = np.append(self.data, new_data)

    def plot_data(self):
        """PLot the microphone's data."""
        plt.plot(self.data)
        plt.grid()
        plt.show()

    def get_frequency(self, t):
        fft_result = np.fft.fft(self.data)
        freq = np.fft.fftfreq(t.shape[-1])

        #plt.plot(freq, np.abs(fft_result))
        #plt.show()
        return fft_result, freq

