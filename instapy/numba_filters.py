"""numba-optimized filters"""
from numba import jit
import numpy as np


@jit(forceobj=True)
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    r, g, b = image[:,:,[0]], image[:,:,[1]], image[:,:,[2]]
    gray_image[:,:] = (r*0.21 + g*0.72 + b*0.07)
    gray_image = gray_image.astype("uint8")
    return gray_image


@jit(forceobj=True)
def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    for i in range(3):
        val = (r*sepia_matrix[i,0] + g*sepia_matrix[i,1] + b*sepia_matrix[i,2])
        val[val > 255] = 255
        sepia_image[:,:,i] = val

    # Return image
    # don't forget to make sure it's the right type!
    sepia_image = sepia_image.astype("uint8")
    return sepia_image