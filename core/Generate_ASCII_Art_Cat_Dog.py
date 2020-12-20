import numpy as np
import sys
import pickle
from zipfile import ZipFile
from PIL import Image

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
				print(file)
				img = Image.open(file)
				print(np.array(img.getdata()).shape, img.size)
				img_list.append(np.array(img.getdata()).reshape((img.size[0], img.size[1], 3)))
				counter += 1

				if counter % 1000 == 0:
					print("Saved", counter, "images")
					print(len(img_list))
					pickle.dump(img_list, open("img_ascii_array.p", "wb"))

	return img_list


if __name__ == '__main__':
	filename = sys.argv[1]
	read_images_from_zip_to_array(filename, invalid_filenames = ['train/'])
