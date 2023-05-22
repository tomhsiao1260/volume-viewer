import os
import numpy as np
import tifffile as tiff

size = { 'w': 249, 'h': 85, 'd': 100 }
TIF_DIR = './res/surface_volume/'


if not os.path.exists('res'):
    os.makedirs('res')
if not os.path.exists('res/surface_volume'):
    os.makedirs('res/surface_volume')

for i in range(size['d']):
    image = np.zeros((size['h'], size['w']), dtype=np.uint16)

    radius = i
    center_x = size['w'] // 2
    center_y = size['h'] // 2

    y_indices, x_indices = np.ogrid[:size['h'], :size['w']]
    circle_mask = (x_indices - center_x) ** 2 + (y_indices - center_y) ** 2 <= radius ** 2
    image[circle_mask] = np.iinfo(np.uint16).max

    filename = f'{TIF_DIR}{i:05d}.tif'
    tiff.imwrite(filename, image)

