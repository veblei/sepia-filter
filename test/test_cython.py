from instapy.cython_filters import cython_color2gray, cython_color2sepia
import numpy as np


def test_color2gray(image, reference_gray):
    result = cython_color2gray(image)
    # check if right shape and dtype
    assert result.shape == image.shape
    assert result.dtype == image.dtype
    # check if the implementation is correct
    assert (result == reference_gray).all()
    # check uniform rgb values
    assert (result[:,:,[0]] == result[:,:,[1]]).all()
    assert (result[:,:,[1]] == result[:,:,[2]]).all()


def test_color2sepia(image, reference_sepia):
    result = cython_color2sepia(image)
    # check if right shape and dtype
    assert result.shape == image.shape
    assert result.dtype == image.dtype
    # check if the implementation is correct
    assert (result == reference_sepia).all()
    # verify pixel samples according to sepia matrix
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
