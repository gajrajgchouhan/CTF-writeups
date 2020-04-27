flag = "h1_th3r3_1ts_m3"
encrypted_flag = "ÐdØÓ§åÍaèÒÁ¡"

key = ""

for i in range(len(flag)):
	key += chr(ord(encrypted_flag[i])-ord(flag[i]))

print(key)