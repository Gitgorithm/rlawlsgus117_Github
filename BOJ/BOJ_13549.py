import sys
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < max and not time[next_step]:
                if next_step == v*2:
                    q.appendleft(next_step)
                    time[next_step] = time[v]

                else:
                    q.append(next_step)
                    time[next_step] = time[v] +1


n, k = map(int, sys.stdin.readline().split(' '))
max = 100001
time = [0]*max
bfs()
