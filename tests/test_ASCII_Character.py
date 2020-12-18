import pytest
import numpy as np
from core.ASCII_Character import ASCII_Character


'''
Test Strategy:
    get_character(): partition on all ASCII character ordinals from 32 to 126 inclusive
    get_character_pixel_array(): partition on the number of black pixels: 0, >0
    get_intensity(): partition on the output of the intensity: 0, >0
'''

'''
    Helper method to test the characters
    param:  char                the ASCII_Character to test
            expect_char         the expected character that char represents
            expect_array        the expected pixel array that char returns
            expect_intensity    the expected intensity (ratio of black vs total pixels) needed
'''
def test_helper(char, expect_char, expect_array, expect_intensity):
    assert char.get_character() == expect_char
    assert np.array_equal(expect_array, char.get_character_pixel_array())
    assert char.get_intensity() - expect_intensity < 1e-5 

def test_assertion_true():
    assert True

'''
    covers get_character(): [SPACE] (ord = 32)
           get_character_pixel_array(): 0 black pixels
           get_intensity(): output = 0
'''
def test_space_character():
    space_char = ASCII_Character(' ')
    array_output = np.ones((11, 6))
    intensity_output = 0.0

    test_helper(space_char, ' ', array_output, intensity_output)

'''
    covers  get_character(): 8 
            get_character_pixel_array(): >0 black pixels
            get_intensity(): > 0
'''
def test_character_8():
    char8 = ASCII_Character('8')
    array = np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1, 1],
                    [0, 0, 1, 0, 0, 1],
                    [0, 0, 1, 0, 0, 1],             
                    [1, 0, 0, 0, 1, 1],
                    [0, 0, 1, 0, 0, 1],
                    [0, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]])
    intensity = 25/66

    test_helper(char8, '8', array, intensity)
