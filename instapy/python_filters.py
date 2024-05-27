"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    i = 0
    for nd in image:
        j = 0
        for row in nd:
            rgb = []
            for item in row:
                rgb.append(item)
            gray_image[i,j] = (rgb[0]*0.21 + rgb[1]*0.72 + rgb[2]*0.07)
            j += 1
        i += 1
    gray_image = gray_image.astype("uint8")
    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ]
    i = 0
    for nd in image:
        j = 0
        for row in nd:
            rgb = []
            for item in row:
                rgb.append(item)
            for h in range(3):
                val =  (rgb[0]*sepia_matrix[h][0] + rgb[1]*sepia_matrix[h][1] + rgb[2]*sepia_matrix[h][2])
                if val > 255:
                    val = 255
                sepia_image[i,j,h] = val
            j += 1
        i += 1
    # Return image
    # don't forget to make sure it's the right type!
    sepia_image = sepia_image.astype("uint8")
    return sepia_image
