from PIL import Image

with open('filesinname.txt') as f:
	locations = [i.strip() for i in f.readlines()]
with open('imgarray.txt') as f:
	im = [i.strip() for i in f.readlines()]
h,w = 299+1,299+1

img = Image.new('RGB',(h,w))
data = img.load()
# h,w = 0,0
c = 0
for location in locations:
	x,y = [int(i) for i in location.split()]
	r, g, b = eval(im[c])
	data[x,y] = (r, g, b)
	c += 1
	# h,w = max(h,int(x)), max(w,int(y))
img.save('twoqrs.png')
# zbarimg twoqrs.png 
# QR-Code:rtcp{d1d-you_d0_7his_by_h4nd?} # Rick Rolled :P
# QR-Code:https://www.youtube.com/watch?v=dQw4w9WgXcQ
# scanned 2 barcode symbols from 1 images in 0.01 seconds

