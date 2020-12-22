import numpy as np
from core.ASCII_Character import ASCII_Character
from PIL import Image

class Image_Conversion:

    '''
    Return the img_array in greyscale
    param:  img_array   an array with 3 dimensions where the first two dimensions are
                        the size of the image and third dimension is size RGB
    return: an 2d array of the same size as the first two dimensions in img_array
    '''
    def rgb_to_greyscale(img_array):
        return 0.299*img_array[:, :, 0]+0.587 * img_array[:, :, 1]+0.114*img_array[:,:,2]

    '''
    Return the img_array using ASCII_Art
    param:  img_array   an array of 2 dimensions where the first two dimensions are the
                        the size of the image. img_array must have a size of at least (11,6)
                        (number of rows, number of cols)
            row_scale (default = 2): the number of rows to match the region
            col_scale (default = 1): the number of columns to match the region
    return: an 2d array uses ASCII Art 
    '''
    def greyscale_to_ascii(img_array, row_scale = 2, col_scale = 1):
        intensity_to_ascii = Image_Conversion.get_intensity_to_ascii()

        ASCII_ROWS = 11
        ASCII_COLS = 6

        nrows = ASCII_ROWS * img_array.shape[0]//row_scale
        ncols = ASCII_COLS * img_array.shape[1]//col_scale

        new_array = np.zeros((nrows, ncols))

        new_row = 0
        new_col = 0
        for r in range(0, img_array.shape[0], row_scale):
            for c in range(0, img_array.shape[1], col_scale):
                if(new_col + ASCII_COLS > ncols):
                    new_col = 0
                    new_row += ASCII_ROWS
                if(new_row + ASCII_ROWS > nrows):
                    break

                intensity = Image_Conversion.get_closest_ascii_intensity(intensity_to_ascii.keys(), 
                                                        np.mean(img_array[r:r+row_scale,c:c+col_scale]))
                new_array[new_row:new_row+ASCII_ROWS,new_col:new_col+ASCII_COLS] = intensity_to_ascii[intensity].get_character_pixel_array()
                new_col += ASCII_COLS

        return new_array

    '''
    Return the img_array after applying conversion_list
    param: img_array        the initial image array
    param: conversion_list  the list of funtions to convert the img_array
                            img_array follows the precondition of conversion_list[0].
                            For each pair (conversion_list[i], conversion_list[i+1]),
                            the output of conversion_list[i] follow the precondition 
                            of conversion_list[i+1]
    '''
    def convert_pipeline(img_array, conversion_list):
        output = img_array
        for conversion in conversion_list:
            output = conversion(output)
        return output

    # Helper Method
    # get a intensity to ASCII_Character
    def get_intensity_to_ascii():
        intensity_to_ascii = {}

        for i in range(32, 127):
            ascii_char = ASCII_Character(chr(i))
            intensity_to_ascii[ascii_char.get_intensity()] = ascii_char

        return intensity_to_ascii

    # get the closest intensity given current_intensity
    def get_closest_ascii_intensity(ascii_intensities, current_intensity):
        min_intensity = -1
        min_diff = 100


        for intensity in ascii_intensities:
            #print(current_intensity, intensity)
            if(abs(current_intensity - intensity) < min_diff):
                min_diff = abs(current_intensity - intensity)
                min_intensity = intensity

        return min_intensity