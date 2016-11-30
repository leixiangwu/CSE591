import time
import sys

#http://www.math.umn.edu/~garrett/crypto/Code/FastPow_Python.html
def f(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

x = 55
e = 1171
m = 111233

if(len(sys.argv) > 1):
	x = int(sys.argv[1])

if(len(sys.argv) > 2):
	e = int(sys.argv[2])

if(len(sys.argv) > 3):
	m = int(sys.argv[3])

start = time.time()
print(f(x,e,m))
print(time.time()-start)

start = time.time()
print(pow(x,e,m))
print(time.time()-start)
