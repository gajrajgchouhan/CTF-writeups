# easyphp | 0CTF Quals 2020

This was a php challenge where the website would just eval the code you provided in the get request.
At first I thought about using something like system or exec, but those functions and others like shell_exec were disabled. 
We can verify that by executing ```phpinfo();``` and checking the functions listed in ```disabled_function``` class.
So running any clever system code or something like a shell was out of question.
Also look out for `open_basedir` in the php configuration you get from `phpinfo();`. Luckily for us it was set to `/` so we could explore the file system easily.

Using ` __DIR__ `, `scandir`, we can quickly check which subdirectory the website is running. There was only `index.php` in `/var/www/html`.
In the `/` directory, we will find `flag.so` and `flag.h` (along with `.dockerenv` folder, `start.sh`) , catting out `flag.so` (you can use `highlight_file`) will give the flag as it was hardcoded in the binary.

`FLAG : flag{FFi_1s_qu1T3_DANg1ouS}`

```python
import requests
url = "http://pwnable.org:19260"
# payload = """echo $s = base64_encode(readfile("../../../flag.so"));"""
# payload = """$f = scandir("/var/www/html");var_dump($f);""" 
# payload = """$f = highlight_file('/start.sh');var_dump($f);"""
r = requests.Session()
print(payload)
print()
s = r.get(url+"?rh="+payload)
final = s.text
print(final)
r.close()
```