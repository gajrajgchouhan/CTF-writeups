import codecs, base64,pwn
def checkpass():
  userinput = input("Enter the password: ")
  key = "nyameowpurrpurrnyanyapurrpurrnyanya"
  key = codecs.encode(key, "rot_13")
  a = nope(key,userinput)
  b = str.encode(a)
  c = base64.b64encode(b, altchars=None)
  c = str(c)
  d = codecs.encode(c, 'rot_13')
  result = wow(d)
  if result == "'=ZkXipjPiLIXRpIYTpQHpjSQkxIIFbQCK1FR3DuJZxtPAtkR'o":
      return True
  else:
      return False
def nope(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def wow(x):
  return x[::-1]

key = "nyameowpurrpurrnyanyapurrpurrnyanya"
key = codecs.encode(key, "rot_13")
result = "'=ZkXipjPiLIXRpIYTpQHpjSQkxIIFbQCK1FR3DuJZxtPAtkR'o"
d = wow(result)
c = codecs.decode(d, 'rot_13')[2:-1]
b = base64.b64decode(c)
b = b.decode()
print(b)
a = nope(key, b)
print(a)