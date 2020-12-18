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
    Method to test the get_character
    param:  char                the ASCII_Character to test
            expect_char         the expected character that char represents
'''
@pytest.mark.parametrize(
    "char,expected_char",
    [(ASCII_Character(' '), ' '), (ASCII_Character('8'), '8')],
)
def test_ascii_get_character(char, expected_char):
    assert char.get_character() == expected_char

'''
    Method to test get_character_pixel_array()
    param:  char            the ASCII Character
            expected_arr    the expected output of the array 
'''
@pytest.mark.parametrize(
    "char,expected_arr",
    [(ASCII_Character(' '), np.ones((11, 6))), 
    (ASCII_Character('8'), np.array([[1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1],
                                    [1, 0, 0, 0, 1, 1],
                                    [0, 0, 1, 0, 0, 1],
                                    [0, 0, 1, 0, 0, 1],             
                                    [1, 0, 0, 0, 1, 1],
                                    [0, 0, 1, 0, 0, 1],
                                    [0, 0, 1, 0, 0, 1],
                                    [1, 0, 0, 0, 1, 1],
                                    [1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1]]))],
)
def test_ascii_get_array(char, expected_arr):
    assert np.array_equal(expected_arr, char.get_character_pixel_array())

'''
    Method to test get_intensity
    param:  char                the ASCII Character
            expected_intensity  the expected intensity 
'''
@pytest.mark.parametrize(
    "char,expected_intensity",
    [(ASCII_Character(' '), 0), (ASCII_Character('8'), 25/66)],
)
def test_ascii_get_intensity(char, expected_intensity):
    assert char.get_intensity() - expected_intensity < 1e-5 
