import zipfile
zipfilename = '1815.zip'
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
			exit(0)
print('Try other')