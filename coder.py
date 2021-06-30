from PIL import Image
import numpy as np

PATH = "tesla.bmp"
message = "B"

image = np.array(Image.open(PATH))
height, width , colors = image.shape

for i, bit in enumerate(bytearray(message+"\0", 'utf8')):
	print(bin(bit))
	for j in range(8):
		v = i * 8 + 7 - j
		print(image[v//height][v%height],end='')
		image[v//height][v%height][0] = 0#image[v//height][v%height][0]//2*2 + bit%2
		print(image[v//height][v%height])
		bit //= 2

im = Image.fromarray(image)
im.save(f'c{PATH}')