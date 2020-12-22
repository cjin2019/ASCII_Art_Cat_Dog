import numpy as np
import sys
import pickle
from zipfile import ZipFile
from PIL import Image

from Image_Conversion import Image_Conversion

# https://stackoverflow.com/questions/33166316/how-to-read-an-image-inside-a-zip-file-with-pil-pillow

'''
	Return a list of the image arrays
	param: filename the name of the zip file containing the images
		   invalid_filenames a collection of filenames that should not be read
		   default value is an empty list
'''
def read_images_from_zip_to_array(filename, invalid_filenames = []):
	img_list = []
	counter = 0

	with ZipFile(filename) as archive:
		for entry in archive.infolist():
			if(entry.filename in invalid_filenames):
				continue
			#added this line due to memory overflow
			# if('cat' in entry.filename):
			# 	continue

			with archive.open(entry) as file:
				img = Image.open(file)
				img_list.append(np.array(img))
				ascii_array = Image_Conversion.convert_pipeline(1 - np.array(img)/255, 
					[Image_Conversion.rgb_to_greyscale, Image_Conversion.greyscale_to_ascii]).astype('uint8')

				# ascii_array[ascii_array == 0] = 1
				ascii_array[ascii_array == 1] = 255
				Image.fromarray(ascii_array.astype('uint8'), "L").save("new_cat.png")

				counter += 1

				# add this line to test only one image
				if(counter == 1):
					break

				if counter % 1000 == 0:
					print("Saved", counter, "images")
					print(len(img_list))
					pickle.dump(img_list, open("img_ascii_array.p", "wb"))

	return img_list


if __name__ == '__main__':
	filename = sys.argv[1]
	read_images_from_zip_to_array(filename, invalid_filenames = ['train/'])
