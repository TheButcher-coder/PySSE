import numpy as np
import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec


p = piss.PySSe()
p.set_x(10)
p.set_y(10)
p.set_dx(.1)

p.add_obj(circ(0, 0, 3, 2*np.pi))


p.run_sim()