from Crypto.Util.number import long_to_bytes
from PIL import Image
import os
filesinname,files, array = open('filesinname.txt','w'), open('files.txt','w'), open('imgarray.txt','w')
c = 0
for file in os.listdir('./chall/'):
	files.write(file+'\n')
	filesinname.write(repr(long_to_bytes(int(file[:-4])))[2:-1]+'\n')
	with Image.open(os.path.join('./chall/',file)) as f:
		u = list(f.getdata())
	print(f'Doing file {c}')
	array.write(repr(u[0])+'\n')
	c += 1
files.close()
array.close()
