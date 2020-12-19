import pytest
import numpy as np
from core.Image_Conversion import Image_Conversion

'''
    Checks to see if rgb_to_greyscale works for 1x1x3 image
'''
def test_rgb_to_greyscale_1_1_3():
    arr = Image_Conversion.rgb_to_greyscale(np.random.randint(256, size = 3).reshape((1,1,3))/255)
    assert arr.shape[0] == 1
    assert arr.shape[1] == 1
    assert np.any((arr <= 1) & (arr >= 0))

'''
    Checks to see if rgb_to_greyscale works for 10x10x3 image
'''
def test_rgb_to_greyscale_10_10_3():
    array = Image_Conversion.rgb_to_greyscale(np.random.randint(256, size = 300).reshape((10,10,3))/255)
    assert array.shape[0] == 10
    assert array.shape[1] == 10
    assert np.any((array >= 0) & (array <= 1))

'''
    Checks to see if greyscale_to_ascii works for 11x6 image
'''
def test_greyscale_to_ascii_11_6():
    array = Image_Conversion.greyscale_to_ascii(np.random.randint(256, size = 66).reshape((11,6))/255)

    unique, counts = np.unique(array, return_counts = True)
    freq = dict(zip(unique, counts))
    assert 0 in freq.keys()
    assert 1 in freq.keys()
    assert 2 == len(freq.keys())

'''
    Checks to see if greyscale_to_ascii works for a bigger image
'''
def test_greyscale_to_ascii_500_500():
    array = Image_Conversion.greyscale_to_ascii(np.random.randint(256, size = 300 * 300).reshape((300,300))/255)

    unique, counts = np.unique(array, return_counts = True)
    freq = dict(zip(unique, counts))
    assert 0 in freq.keys()
    assert 1 in freq.keys()
    assert 2 == len(freq.keys())

'''
    Checks to see if convert_pipeline works for rgb_to_greyscale -> greyscale_to_ascii
'''
def test_convert_pipeline():
    inp = np.random.randint(256, size = 500*500*3).reshape((500,500,3))/255
    array = Image_Conversion.convert_pipeline(inp, [Image_Conversion.rgb_to_greyscale, Image_Conversion.greyscale_to_ascii])
    
    unique, counts = np.unique(array, return_counts = True)
    freq = dict(zip(unique, counts))
    assert 0 in freq.keys()
    assert 1 in freq.keys()
    assert 2 == len(freq.keys())

