"""Cython implementation of filter functions"""

import numpy as np
cimport numpy as np

cpdef cython_color2gray(image):
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef np.ndarray gray_image = np.empty_like(image)
    cdef np.ndarray r = image[:,:,[0]]
    cdef np.ndarray g = image[:,:,[1]]
    cdef np.ndarray b = image[:,:,[2]]
    gray_image[:,:] = (r*0.21 + g*0.72 + b*0.07)
    gray_image = gray_image.astype("uint8")
    return gray_image


cpdef cython_color2sepia(image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    cdef np.ndarray sepia_image = np.empty_like(image)

    cdef np.ndarray sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    cdef np.ndarray r = image[:,:,0]
    cdef np.ndarray g = image[:,:,1]
    cdef np.ndarray b = image[:,:,2]
    cdef int i
    cdef np.ndarray val
    for i in range(3):
        val = (r*sepia_matrix[i,0] + g*sepia_matrix[i,1] + b*sepia_matrix[i,2])
        val[val > 255] = 255
        sepia_image[:,:,i] = val
        
    sepia_image = sepia_image.astype("uint8")
    return sepia_image
