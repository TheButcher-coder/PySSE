import numpy as np
import matplotlib.pyplot as plt

import src.PySSE as piss
from src.Line import Line
from src.circ import circ
from src.rec import rec
from src.speaker_line import speaker_line

# Maßstabsfaktor: mm → m
scale = 1 / 1000

# Originalmaße (mm)
R = 250
L_total = 983.92
cutout_width = 626.6
cutout_height = 400
cutout_offset = 275.7
cutout_angle_deg = 22.4
angle_rad = np.radians(cutout_angle_deg)

# In Meter umgerechnet
R *= scale
L_total *= scale
cutout_width *= scale
cutout_height *= scale
cutout_offset *= scale

# Geometriepunkte
x0, y0 = R, R
x1 = x0 + np.cos(angle_rad) * 0.6  # geschätzt
y1 = y0 + np.sin(angle_rad) * 0.6

x_cut_left = cutout_offset
y_cut_bottom = y1
x_cut_right = x_cut_left + cutout_width
y_cut_top = y_cut_bottom + cutout_height

# Initialisiere Simulation
p = piss.PySSe()
p.set_dx(.001)
p.set_x(1.2)
p.set_y(1.2)
p.set_tmax(200)

p.set_source_x(0.1)
p.set_source_y(0.6)

# Gehäuseobjekte
p.add_obj(circ(R, R, R, 270, 360))                              # untere Rundung
p.add_obj(Line(R, R, x1, y1))                                   # Schräge Linie
p.add_obj(Line(x_cut_left, y_cut_top, x_cut_right, y_cut_top)) # Rechteck oben
p.add_obj(Line(x_cut_right, y_cut_top, x_cut_right, y_cut_bottom))
p.add_obj(Line(x_cut_right, y_cut_bottom, x_cut_left, y_cut_bottom))
p.add_obj(Line(x_cut_left, y_cut_bottom, x_cut_left, y_cut_top))
p.add_obj(circ(R, L_total - R, R, 0, 90))                       # obere Rundung

# Lautsprecher und Mikrofon
p.add_obj(speaker_line(0.0, 0.25, 0.2, 0.25))
p.add_mic(0.9, 0.25)

p.print()
plt.show()