from codecs import encode, decode
flag = list("b00t2root{}")

encoded = "035e44154106060c17181b"
decoded = list(decode(encoded, 'hex'))
print(decoded)
print(list(map(ord, flag)))


real_flag = []
for i in range(11):
    real_flag.append(ord(flag[i]) ^ decoded[i])

real_flag = "b00t2root{" + "".join(map(chr, real_flag)) + "}"
print(real_flag)
# assert len(real_flag) == 22

# c = xor(real_flag[:11], real_flag[11:])
# c = encode(c.encode(), 'hex')
# print(c)
# assert c.decode() == encoded
