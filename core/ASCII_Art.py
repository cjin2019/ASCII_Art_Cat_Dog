from PIL import Image, ImageDraw, ImageFont
import numpy as np

class ASCII_Art_Character:

    '''
    field:
    character is a string of length 1 where 32 <= ASCII ordinal <= 126
    '''

    '''
    Creates an ASCII_Art_Character 
    param: character is a string of length 1 
           where 32 <= ASCII ordinal <= 126
    '''
    def __init__(self, character):
        self.character = character

    '''
    Returns the ASCII charater of this
    '''
    def get_character():
        return self.character

    '''
    Returns the numpy array representation of the ASCII character
    '''
    def get_character_pixel_array():
        return None

    '''
    Returns the intensity of the character 
    '''
    def get_intensity():
        return 0

