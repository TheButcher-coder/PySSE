import numpy as np
import matplotlib.pyplot as plt

import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec


def delta(t):
    """
    Delta function for the source.
    """
    amp = 1
    if t == 0:
        return amp
    else:
        return 0


p = piss.PySSe()
p.set_x(10)
p.set_y(10)
p.set_dx(.1)
p.set_source_x(5)
p.set_source_y(5)
p.set_tmax(10000)

#small example with bass reflex housing
p.add_obj(Line(1, 1, 6, 1))  # bottom
p.add_obj(Line(6, 2, 6, 6))  # right side
p.add_obj(Line(6, 2, 2, 2))  # tube
p.add_obj(Line(6, 6, 1, 6))  # top
p.add_obj(Line(1, 6, 1, 1))  # left side
p.add_mic(70, 15)

x = p.run_sim(inp_fun=delta, plot=False)
y = p.get_mic_data()

datax = np.fft.fft(x)
fx = np.fft.fftfreq(x.shape[-1], d=p.get_dt())
datay = np.fft.fft(y)
fy = np.fft.fftfreq(y.shape[-1], d=p.get_dt())

G = datay / datax
plt.semilogx(fx, 20* np.log10(np.abs(G)), label='Gain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid()
plt.show()