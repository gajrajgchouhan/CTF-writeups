flags = list("øz§è§ñy÷¦")
for i in range(0,len(flags)):
	flags[i] = chr(ord(flags[i])-20)
encrypted_flag = flags + list("ÄÑÓ¿ÂÒêá")
flag = "r34l_g4m3rs_eXclus1v3" # 21
input = [0]*len(flag)
input[7] = 'u'
input[0:2] = 'h0'

for i in range(0, len(flag)-14):
	x = encrypted_flag[0:7]
	input[i+8] = chr(ord(x[i])-ord(flag[i]))
for i in range(10, len(flag)-6):
	x = encrypted_flag[7:7+5]
	input[i-8] = chr(ord(x[i-10]) - ord(flag[i]))
i = 15
while (i < len(flag)):
	x = encrypted_flag[7+5:7+5+6]
	input[i] = chr(ord(x[i-15]) - ord(flag[i-3]))
	i += 1
print(''.join(input))