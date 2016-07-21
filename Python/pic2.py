from PIL import Image

darkBlue= (0,51,76)
red = (217,26,33)
lightBlue = (112,150,158)
yellow = (252,227,166)

im = Image.open("owlapple.jpg")
width = im.size[0]
height = im.size[1]
pl = list(im.getdata())
pic = Image.new("RGB",(width,height))
pl2 = list()
for p in pl:
	intensity = sum(p)
	if intensity < 182:
		pl2.append(darkBlue)
	elif intensity >= 182 and intensity <364: 
		pl2.append(red)
	elif intensity >= 364 and intensity<546: 
		pl2.append(lightBlue)
	else: 
		pl2.append(yellow)
pic.putdata(pl2)
pic.show()