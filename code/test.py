#chatgpt generated test

import numpy as np
import matplotlib.pyplot as plt

# Gitterparameter
Nx, Ny = 100, 100
dx = 0.01  # 1 cm Auflösung
dt = dx / (np.sqrt(2) * 343)  # CFL-Bedingung
steps = 500

# Druckfelder
p = np.zeros((Nx, Ny))
p_old = np.zeros((Nx, Ny))
p_new = np.zeros((Nx, Ny))

# Anregung in der Mitte
src_x, src_y = Nx//2, Ny//2

# Simulationsschleife
for t in range(steps):
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            laplacian = (p[i+1, j] + p[i-1, j] + p[i, j+1] + p[i, j-1] - 4*p[i, j]) / dx**2
            p_new[i, j] = 2*p[i, j] - p_old[i, j] + (343**2) * dt**2 * laplacian

    # Quelle als kurzer Impuls
    if t < 5:
        p_new[src_x, src_y] += np.sin(2 * np.pi * 500 * dt * t)

    p_old, p = p, p_new.copy()

    if t % 50 == 0:
        plt.imshow(p, cmap='RdBu', vmin=-0.01, vmax=0.01)
        plt.title(f"t = {t}")
        plt.pause(0.01)

plt.show()
