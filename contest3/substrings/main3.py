#! /usr/python

mval = 10**9 + 7
a = raw_input()
n = len(a)
gs = 0
os = 0
k =  0
for i in range(n):
    k = k+1
    ns = (os * 10 + k * int(a[i])) % mval
    gs = (gs + ns) % mval
    os = ns
print gs