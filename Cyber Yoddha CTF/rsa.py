from Crypto.Util.number import long_to_bytes, inverse

ct1 = 23441987
ct2 = 31018357

n = 52035749
p, q = 6571, 7919

e = 101

phi = (p-1)*(q-1)

d = inverse(e, phi)
m = pow(ct1, d, n)

print(m*(1e-6))

d = inverse(e, phi)
m = pow(ct2, d, n)

print(m*(1e-6))
