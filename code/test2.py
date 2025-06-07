import numpy as np
import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec


p = piss.PySSe()
p.set_x(100)
p.set_y(100)
p.set_dx(.1)

p.add_obj(Line(00, 0, 100, 100))

p.print()

p.run_sim()