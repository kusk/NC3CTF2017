from PIL import Image
im = Image.open('billede.png')
rgb_im = im.convert('RGB')

f = open('secret', 'w')

vert = 0
horz = 0

while horz < 300:
	r, g, b = rgb_im.getpixel((horz, vert))
	horz = horz+1
	color = str(r)+'-'+str(g)+'-'+str(b)
	if color == '0-0-0':
		f.write('x2A')
	elif color == '0-128-126':
		f.write('x0B')
	elif color == '0-255-36':
		f.write('x3F')
	elif color == '18-0-255':
		f.write('x34')
	elif color == '246-0-255':
		f.write('x1E')
	elif color == '255-0-0':
		f.write('x4B')
	elif color == '255-204-233':
		f.write('x78')
	elif color == '255-246-0':
		f.write('xB6')
	else:
		print(color)

	if vert == 299 and horz == 299:
		break
	elif horz == 299:
		vert = vert+1
		horz = 0


f.close()