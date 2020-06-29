from pwn import *
from ctypes import CDLL
import time
libc = CDLL('libc-2.31.so')

addr = 'iitmandi.co.in'
operation = ['+', '-', '*']

s = remote(addr, 9696)
# Seed srand with time(0)
now = int(time.time())
libc.srand(now)

s.recv()
s.send(b'2\n')

def predictMath():
    a = libc.rand() % 100
    b = libc.rand() % 100
    op = operation[libc.rand() % 3];
    print("MINE {}{}{}?".format(a,op,b))

def predictSlot():
    lot_chars = ['$', '%', '&', '*', '#', '?', '@']
    a_lot = lot_chars[libc.rand() % 7]
    b_lot = lot_chars[libc.rand() % 7]
    c_lot = lot_chars[libc.rand() % 7]
    print("MY PREDICTION : {} {} {}".format(a_lot,b_lot,c_lot))
    return a_lot==b_lot==c_lot

predictMath()
q = s.recv().split()[-1]
print("THEIR {}".format(q.decode()))
ans = repr(eval(q[:-1]))
s.sendline(ans.encode())

for i in range(49):
    predictMath()
    q = s.recv().strip()
    print("THEIR {}".format(q.decode()))
    ans = repr(eval(q[:-1]))
    s.sendline(ans.encode())

money = 1000
print(s.recv())
for i in range(20):
    print(money)
    pred = predictSlot()
    if pred:
        s.sendline('1000')
        money += 1000
    else:
        s.sendline('-10000')
        money += 10000
    slot = s.recv().decode()
    print(slot)
    if 'Spinning the reels' not in slot:
        break

#FLAG : dante{7he_h19hes7_weal7h_1s_7he_a8sence_0f_9reed}