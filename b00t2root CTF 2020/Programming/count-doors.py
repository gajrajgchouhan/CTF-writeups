N = 898399329838283293892392328398239832
from math import sqrt, floor
# N = 2 * 2 * 2 * 19 * 5910521906830811144028896897356841

def solve(N):
    arr = [None] + [0]*N

    for i in range(1, N+1):
        for j in range(i, N+1, i):
            arr[j] ^= 1

    return sum(arr[1:])

def solve2(N):
    return floor(sqrt(N))

print(f'b00t2root{{{solve2(N)}}}')