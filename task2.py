import numpy as np
import os

address_in = 'matrix_24_2.npy'

matrix = np.load(address_in)

x = list()
y = list()
z = list()

limit = 500 + 24

size = len(matrix)

for i in range(size):
    for j in range(size):
        elem = matrix[i][j]
        if(elem > limit):
            x.append(i)
            y.append(j)
            z.append(elem)

np.savez('points', x = x, y = y, z = z)
np.savez_compressed('points_zip', x = x, y = y, z = z)

print(f"points = {os.path.getsize('points.npz')}")
print(f"points_zip = {os.path.getsize('points_zip.npz')}")

