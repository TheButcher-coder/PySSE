import numpy as np
import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec


p = piss.PySSe()
p.set_x(4)
p.set_y(4)
p.set_dx(.1)
#p.add_obj(rec(-1, -1, 1, 1))
p.add_obj(circ(0, 0, 100, np.pi, np.pi))
#p.add_obj(l.Line(-1, 0, 1, 0))
p.print()

p.run_sim()