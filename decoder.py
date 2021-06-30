from PIL import Image
import numpy as np #28E0EA

PATH = "ctesla.bmp"
message = ''

image = np.array(Image.open(PATH))
height, width , colors = image.shape

print(image[0][:8*3])

# i = 0
# while "\0" not in message and i < 2:
# 	c = 0
# 	for j in range(8):
# 		v = i * 8 + j
# 		print(image[v//height][v%height][0],' ',image[v//height][v%height][0]%2)
# 		c += image[v//height][v%height][0]%2
# 		c *= 2
# 	print(' ',chr(c))
# 	message += chr(c)
# 	i += 1

# print(message)