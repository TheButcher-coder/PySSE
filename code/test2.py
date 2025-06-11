import numpy as np
import matplotlib.pyplot as plt

import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec


p = piss.PySSe()
p.set_x(10)
p.set_y(10)
p.set_dx(.1)
p.set_source_x(5)
p.set_source_y(5)
p.set_tmax(500 )

#small example with bass reflex housing
p.add_obj(Line(1, 1, 6, 1))  # bottom
p.add_obj(Line(6, 2, 6, 6))  # right side
p.add_obj(Line(6, 2, 2, 2))  # tube
p.add_obj(Line(6, 6, 1, 6))  # top
p.add_obj(Line(1, 6, 1, 1))  # left side
p.add_mic(70, 15)

p.run_sim(vis_flag=False)  # run simulation without plotting
p.plot_mic_data()

res, freq = p.get_freq()
plt.plot(freq, res)
plt.show()