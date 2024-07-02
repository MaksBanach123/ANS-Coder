import matplotlib.pyplot as plt
import numpy as np


def read_pgm_file(file_path):
    with open(file_path, 'rb') as file:
        # Skip the magic number line
        file.readline()
        
        # Read the width, height, and maxval, skipping any comment lines
        width, height, max_val = None, None, None
        while True:
            line = file.readline().decode('utf-8').strip()
            if not line.startswith('#'):
                parts = line.split()
                if len(parts) == 3:
                    width, height, max_val = map(int, parts)
                    break
                elif len(parts) == 2:
                    # Handle the case where maxval is missing
                    width, height = map(int, parts)
                    max_val = 255 # Default maxval for 8-bit images
                    break
                else:
                    raise ValueError("Invalid PGM file format")
        
        # Ensure we have valid values
        if width is None or height is None or max_val is None:
            raise ValueError("Invalid PGM file format")
        
        # Read the image data
        image = np.fromfile(file, dtype=np.uint8, count=width*height)
        image = image.reshape((height, width))

    return image


def histogram_plot(image):
    hist_2, bin_edges = np.histogram(np.array(image), bins=256, range=(0, 256))

    plt.plot(bin_edges[:-1], hist_2)
    plt.title('Histogram')
    plt.xlabel('Wartość piksela')
    plt.ylabel('Częstość')
    plt.show()


file_path = './rozklady_testowe/normal_50.pgm'
image = read_pgm_file(file_path)
histogram_plot(image)
