from PIL import Image, ImageDraw, ImageFont
import numpy as np

class ASCII_Character:

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
    def get_character(self):
        return self.character

    '''
    Returns the numpy array representation of the ASCII character
    '''
    def get_character_pixel_array(self):
        im = Image.new('1', (6, 11), color = 1)
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), self.character, font = ImageFont.load_default())
        return np.array(im.getdata()).reshape((11,6))

    '''
    Returns the intensity of the character 
    '''
    def get_intensity(self):
        arr = self.get_character_pixel_array()
        shape = arr.shape
        numChars = shape[0] * shape[1]
        return (numChars - sum(sum(arr)))/numChars

