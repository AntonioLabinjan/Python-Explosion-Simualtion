import numpy as np
import matplotlib.pyplot as plt

# Parametri simulacije
grid_size = 100  # Veličina mreže
explosion_radius = 10  # Radijus eksplozije
explosion_strength = 5  # Snaga eksplozije
num_frames = 50  # Broj koraka u animaciji

# Inicijalizacija mreže
grid = np.zeros((grid_size, grid_size))
center = grid_size // 2
grid[center, center] = explosion_strength

# Priprema za animaciju
plt.figure(figsize=(8, 8))
plt.title('Simulacija širenja eksplozije')

for frame in range(num_frames):
    # Računanje novog stanja mreže
    new_grid = np.zeros_like(grid)
    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            new_grid[i, j] = (grid[i, j] +
                              grid[i - 1, j - 1] + grid[i - 1, j] + grid[i - 1, j + 1] +
                              grid[i, j - 1] + grid[i, j + 1] +
                              grid[i + 1, j - 1] + grid[i + 1, j] + grid[i + 1, j + 1]) / 9

    # Primjena eksplozije u središtu
    if frame == 0:
        new_grid[center, center] = explosion_strength

    grid = new_grid

    # Vizualizacija
    plt.imshow(grid, cmap='hot', vmin=0, vmax=explosion_strength)
    plt.colorbar()
    plt.pause(0.1)
    plt.clf()

plt.show()
