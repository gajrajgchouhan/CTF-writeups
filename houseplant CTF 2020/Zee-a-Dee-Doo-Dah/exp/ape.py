import os
import zipfile

def extract(file):
	zipfilename = file
	dictionary = '../xato-net-10-million-passwords-10000.txt'
	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'rb') as f:
		for line in f.readlines():
			password = line.strip()
			try:
				zip_file.extractall(pwd=password)
			except:
				continue
			else:
				password = 'Password found: %s' % password
				print(password)
				return
	print('Try other')

n = 0
while True:
	x = os.listdir('.')
	x = sorted(x, key= lambda c: c.split('.')[0].rjust(4,'0'),reverse=1) # to prevent screwups in sorting, make them 4 digits
	x.remove('ape.py')
	print(x[n])
	if x[n].split('.')[1]=='zip':
		extract(x[n])
	else:
		os.system('7z x -bb '+ f'{x[n]}')
	n += 1
