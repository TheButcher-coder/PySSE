import numpy as np
import matplotlib.pyplot as plt

import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec
from src.speaker_line import speaker_line

p = piss.PySSe()
p.set_dx(.01)
p.set_x(1)
p.set_y(1)

#p.set_dt(.01)
p.set_tmax(1000)

p.set_source_x(.4)
p.set_source_y(.4)

p.add_obj(Line(0, 0, 0, 0.5))  # left
p.add_obj(Line(0, .5, .2, 0.5))
p.add_obj(Line(0, 0, .2, 0))
p.add_obj(Line(.2, .1, .2, 0.4))
p.add_obj(Line(.1, .1, .2, .1))
p.add_obj(Line(.1, .4, .2, 0.4))

p.add_obj(speaker_line(0, .25, .2, .25))

p.add_mic(.75, .25)


x = p.run_sim(plot=False)
y = p.get_mic_data()
while y[0] == 0:
    np.roll(y, -1)
datax = np.fft.fft(x)
fx = np.fft.fftfreq(x.shape[-1], d=p.get_dt())
#fx = np.unwrap(np.angle(datax))
datay = np.fft.fft(y)
#fy = np.fft.fftfreq(y.shape[-1], d=p.get_dt())

G = datay / datax
angle = (np.angle(G))


plt.subplot(2, 1, 1)
plt.semilogx(fx, 20*np.log10(np.abs(G)), label='Gain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.grid()

plt.subplot(2, 1, 2)
plt.semilogx(fx, 180/np.pi*angle, label='Phase')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (Deg)')
plt.grid()
plt.show()

p.print()
plt.show()