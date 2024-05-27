from instapy.python_filters import python_color2gray, python_color2sepia
import numpy as np


def test_color2gray(image):
    # run color2gray
    result = python_color2gray(image)
    # check that the result has the right shape, type
    assert result.shape == image.shape
    assert result.dtype == image.dtype
    # assert uniform r,g,b values
    assert (result[:,:,[0]] == result[:,:,[1]]).all()
    assert (result[:,:,[1]] == result[:,:,[2]]).all()


def test_color2sepia(image):
    # run color2sepia
    result = python_color2sepia(image)
    # check that the result has the right shape, type
    assert result.shape == image.shape
    assert result.dtype == image.dtype
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ]
    assert (
        result[0,0,0] == int(np.sum(image[0,0,:]*sepia_matrix[0][:]))
        or
        result[0,0,0] == 255
    )
    assert (
        result[0,0,1] == int(np.sum(image[0,0,:]*sepia_matrix[1][:]))
        or
        result[0,0,1] == 255
    )
    assert (
        result[0,0,2] == int(np.sum(image[0,0,:]*sepia_matrix[2][:]))
        or
        result[0,0,2] == 255
    )