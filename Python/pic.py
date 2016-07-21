from PIL import Image

darkBlue= (0,51,76)
red = (217,26,33)
lightBlue = (112,150,158)
yellow = (252,227,166)
purple = (160,32,240)
orange = (255,69,0)
green = (0,250,154)
blue = (132,112,255)

im = Image.open("flower.jpg")
width = im.size[0]
height = im.size[1]

for x in range(width):
	for y in range(height):
		intensity = sum(im.getpixel((x,y)))
		if intensity<182: 
			im.putpixel((x,y),purple)
		elif intensity >= 182 and intensity <364: 
			im.putpixel((x,y),blue)
		elif intensity >= 364 and intensity<546: 
			im.putpixel((x,y),green)
		else: 
			im.putpixel((x,y),orange)
		
im.show()