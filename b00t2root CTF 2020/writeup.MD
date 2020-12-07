## b00t2root CTF

- Writeup (Credits to my team!)

#### Try Try Don't Cry

- Decode from hex and base64 using cyberchef
- We get a hex value (035e44154106060c17181b)
- Xor it with flag
- You will get this : antasticccf
- as we pretty much know the flag format is the first 10 characters and 11th could be exchanged with `}` due to commutativity of XOR.
- We get `antasticccf`, now bring `f` to front as the 11th character.
- Flag : `b00t2root{fantasticcc}`

#### Counting Doors

- The number of open doors changed when there is a prime number
- So find number of prime numbers b/w 1 and N
- Thats `floor(root(N))`
- If we directly use floor(sqrt(N)) from math module in python. we get incorrect answer due to floating point errors.
- So using wolframaplha will be better.
- Flag : `b00t2root{947839295365139044}`

#### String Q (Couldn't remember the name)

- Implement the algorithm in a function
- Here we will use the algorithm on dummy data (array) made up of indices of characters of original data.
- Since the data will not be changed, we can map the given and encrypted data
- And get the original data.
- Flag : `b00t2root{@The_Director_is_the_bot}`

#### Active Directory

- just a active directory exploit
- unzip the archive, and decrypt the password in groups.xml 
- Flag : `b00t2root{Grp_p0l1c13s_sUck}`

- https://www.jaiminton.com/HTB/Active/#
- Use this ruby script for decoding cPassword
https://raw.githubusercontent.com/BustedSec/gpp-decrypt/master/gpp-decrypt.rb

#### Osint 1-3

- Instagram : `redjohn190989`
- We get a morse code.
- `FELIPEPANTONE`
- ```Flag : boot2r00t{m0rs3_d3cod3r_i5_fun}
There is a twitter account with the same name.```

- Twitter : @RedJohn05844438
- Wikipedia : https://en.wikipedia.org/w/index.php?title=Red_John&action=history
- `<!-- Red John says : https://cutt.ly/3hjieDT -->`
- got image
- ^BENJAMINNETANYAHU
- ```Flag : b00t2root{1nf0rmat10n_1n_pl@in_5ight}
Maybe going WAYBACK can help you out.```

- `Critical op intel on reddit. Give it a look.`
- Reddit : https://pastebin.com/LBV5BvEN
- https://www.reddit.com/user/redjohn190989/comments/k3987y/serious_investigation/

#### Johnny Johnny

- Zip has a file called `PagesOut`
- if we search the file name it can be found on the internet
- after downloading it, we are supposed to use `known plaintext attack` on the given Zip file.
- As we know the file already available in the zip
- I tried on Pkcrack and Bkcrack but they didn't worked.
- Will Update this later
- https://x3ero0.tech/posts/plaintext_attack_on_zip_legacy_crypto/

#### Vulnerable Adventure 1-2

- Since game used py file on our machine
- We can change the py file, to get the flag
- From here : https://github.com/DaBaddest/CTF-Writeups/tree/master/boot2root%202020/Vulnerable%20Adventure

- For Part 1
- Change to posx and posy in our machine

- For Part 2
- Set the dummyflag

#### PCap Tracing

- https://github.com/DarkArmy-ctf/ctf-writeups/tree/master/boot2root/Forensics/PCAP_Tracing

#### BuggyPhp

- we are given a web page which shows 
 ![](./buggyphp/cropped)
- https://www.securify.nl/blog/spot-the-bug-challenge-2018-warm-up
- Used this for passing the hmac step
- Afterwards we have to figure out a way to access the files (`req.php` and `index.php`)
- 
