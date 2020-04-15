# IJCTF 2020 Writeups

All challenge files are avaiable here : [https://github.com/linuxjustin/IJCTF](https://github.com/linuxjustin/IJCTF)

## These are the Pre-CTF challenges.

## Stego

### String

Description : 

Question titles are often important as hints :)
Given a file, if we run the strings command 

```console
kali@kali:~$ strings ijctf.jpg | tail -1
ijctf{always_always_look_at_5tr1ng5}
```
We can use tail -1 to get the last line.

Flag : ijctf{always_always_look_at_5tr1ng5}

### Simple Stego

Description : 

Significant file name is similiar to Least Significant Bit or LSb hmm...
Run zsteg.

```console
kali@kali:~$ zsteg significance.png 
ijctf{LSB_4_s3cr3t_pl4c3_t0_h1d3_d4t4}
```

Flag : ijctf{LSB_4_s3cr3t_pl4c3_t0_h1d3_d4t4}

### Header

Description : 

File header go ! Just google for magic number of png file.Use a hexeditor like bless, but the hexedit in the terminal is pretty handy.

```console
kali@kali:~$ hexedit header.png
```

Flag : ijctf{headers8950}

### Exitfloor

Description : 

This is definetly Exiftool. See the metadata of the given picture on terminal.

```console
kali@kali:~$ exiftool exi.jpg | grep -i ijctf
Owner Name   : ijctf{s0m3_ju1cy_m3t4d4t4}
```

Flag : ijctf{s0m3_ju1cy_m3t4d4t4}

### Snow

Description : 

SNOW is a great tool for this challenge. Use snow.exe for windows or stegsnow for unix.

```console
kali@kali:~$ stegsnow -C readme.txt | grep -i ijctf
flag{Ste6_$n0w!!}
```

Flag : flag{Ste6_$n0w!!}

### Pixel

We are given a .py file which was used for encryption of a 'qr.png'. QR generally contains only black and white, and since the encrypted file also has only two type of hex values we can try encrypting a single black and white pixel.

```python
def magic( pixel ):
	k = 1.158371
	res = (pixel[0]&0x1f)*k+(pixel[1]&0x3f)*k+(pixel[2]&0x7f)*k
	return int( res )
black = (0,0,0)
white = (255,255,255)

print(hex((magic(black))))
print(hex((magic(white))))

# 0x0
# 0xff
```
So the black pixel is 0x0 in encrypted file, and similiarly also white pixel.
We can rebuild the qr image file using this knowledge using python and the pillow library.
```python
from PIL import Image
with open('pixel.enc','rb') as f:
	s = f.read()
l = []
d = []
for i in s:
	l.append((0,0,0) if i==0 else (255,255,255))
for i in range(0,40000,200):
# Length of l is 40,000 meaning qr image height &
# width should be 200,200
	x = l[i:i+200]
	d.append(x)
img = Image.new('RGB',(200,200))

data = img.load()
for i in range(200):
	for j in range(200):
		x,y = i,j
		data[x,y] = d[x][y]

img.show()
img.save('qr.png')
```
You will obtain a qr code, we can scan it using zbarimg to get a paste of base64 text.
Then converting the base64 to image will give the flag.

### Knock Knock

Hint : 'Hide and seek' in description of the challege.

Use the [diit](https://sourceforge.net/projects/diit/), the Digital Invisible Ink toolkit.

## Crypto

### Snow

Description :Help Detective Pikachu To Find The Flag.

```
pi pi pi pi pi pi pi pi pi pi pika pipi pi pipi pi pi pi pipi pi pi pi pi pi pi pi pipi pi pi pi pi pi pi pi pi pi pi pichu pichu pichu pichu ka chu pipi pipi pipi pipi pi pi pi pi pi pikachu pi pikachu ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu pi pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu ka ka pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka pikachu pi pi pikachu ka ka ka ka ka ka ka ka ka ka pikachu pi pi pikachu pi pi pi pi pi pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pikachu pi pi pi pi pi pi pi pi pi pikachu pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka pikachu ka ka ka ka ka ka ka ka ka ka pikachu ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pikachu pi pi pi pi pi pi pi pi pi pi pi pikachu pi pi pi pi pi pi pi pi pi pikachu 
```

This is a esoteric language, called pikalang (Duh).
Use a online decoder for this one.
[http://martin.ingesen.no/Pikalang/]
You get the language made up of +,>,- and ]. This is known as brainfuck.

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++.+.-------.+++++++++++++++++.--------------.+++++++++++++++++++++.-----------------------.+.+++++++++++++++.---------------.--.+++++++++++++++++.-----------.+++++++++++++.-----------------.------.+++++++++++++++++.-------.++.----------.++.+++++.+++++++++++++.----------------------.+++++++.+++++++++.++++++.-------.----------.-----.++++++++++.+++++++++++.+++++++++.
```

[https://tio.run/] has interpreters for a lot of languages including BF.

Flag : ijctf{detective_pikachu_found_it}

### Baby_RSA

Description : 
```
n=79832181757332818552764610761349592984614744432279135328398999.....c=5761634303253945396246958107406452065141290318762099471483671710912958815965982450617263100981569575700961240085974706....
e=65537
```
This is RSA, for given modulus (n), ciphertext (c), exponent (e) we can determine a secret message (m) using mathematics.

Use RSATool or the given python code.

```python
from Crypto.Util.number import inverse, long_to_bytes
n = 
p ,q = # p and q are the factors of n, visit factordb.com to factor n.
e = 
c = 
phi = (p - 1) * (q - 1) 
d = inverse(e,phi) # decryption key

m = pow(c,d,n)

print(repr(long_to_bytes(m)))
```

Flag : ijctf{34sy_but_n3c3ss4ry}

### Snow

Description : 

SNOW is a great tool for this challenge. Use snow.exe for windows or stegsnow for unix.

```console
kali@kali:~$ stegsnow -C readme.txt | grep -i ijctf
flag{Ste6_$n0w!!}
```

Flag : flag{Ste6_$n0w!!}


### RSA

Description : 
```
c = 0x20bda043c2077da0366e10de0ef090e5fe333c36fe0dad0cc389e056bd02bd22726f24...
n = 0xac06baabaab0083b4e123536f479d15bcbd638da90b926fbe3c5985760212b666f45b6...
p + q = 0x1a81a2935987d83fe3cd422f043118adfdc554f46cc526af9e289f87e5427f490870b3cd0835a43c0c49769f8aea11914e6acb061f8d8b5f5ee212a83482b49ca
e = 0x10001
```

Modified RSA, you can't factor n in factordb.com ;)
But you are given p+q.

phi = (p - 1)*(q - 1)
We can rearrange the totient func. or p and q.

phi = n - (p+q) + 1

That's it !

