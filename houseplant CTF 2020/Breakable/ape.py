flag = "k33p_1t_in_pl41n"
encrypted_flag = "ÒdÝ¾¤¤¾ÙàåÐcÝÆ¥ÌÈáÏÜ¦aã"
half_encrypted_flag = encrypted_flag[0:int(len(encrypted_flag)/2)]
other_half_encrypted_flag = encrypted_flag[int(len(encrypted_flag)/2):]
print(len(other_half_encrypted_flag))
print(len(flag),len(encrypted_flag))

real_flag = [0]*len(flag)
for i in range(0,len(flag)-2):
	real_flag[i+2] = chr(ord(half_encrypted_flag[i])-ord(flag[i]))
print(real_flag)
for i in range(2,len(flag)):
	print(i)
	real_flag[i-2] = chr(ord(other_half_encrypted_flag[i-2])-ord(flag[i]))
print(''.join(real_flag))