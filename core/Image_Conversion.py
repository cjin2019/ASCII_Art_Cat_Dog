import numpy as np

class Image_Conversion:

    '''
    Return the img_array in greyscale
    param:  img_array   an array with 3 dimensions where the first two dimensions are
                        the size of the image and third dimension is size RGB
    return: an 2d array of the same size as the first two dimensions in img_array
    '''
    def rgb_to_greyscale(img_array):
        return None

    '''
    Return the img_array using ASCII_Art
    param:  img_array   an array of 2 dimensions where the first two dimensions are the
                        the size of the image. img_array must have a size of at least (11,6)
                        (number of rows, number of cols)
    return: an 2d array uses ASCII Art 
    '''
    def greyscale_to_ascii(img_array):
        return None

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
