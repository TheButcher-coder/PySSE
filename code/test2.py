import numpy as np
import src.PySSE as piss
import src.Line as l, src.circ as c, src.rec as r

p = piss.PySSe()
p.add_obj(r.rec(-1, -1, 1, 1))
p.add_obj(c.circ(0, 0, 1, np.pi, np.pi))
#p.add_obj(l.Line(-1, 0, 1, 0))
p.print()