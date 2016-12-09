import time
import sys

#http://www.math.umn.edu/~garrett/crypto/Code/FastPow_Python.html
def fme1(x,e,m):
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

def naivefme(base, power, mod):
  result = 1
  i = 0
  while i < power:
    result = (result * base) % mod
    i += 1
  return result

# https://webstersprodigy.net/2008/10/19/modular-exponentiation-python-program/
# Convert integer n into a list of bits
# Space of O(log(n)) bits to O(nlogn) bits
def binconvert(n):
  barray = []
  if n < 0: 
    raise ValueError, "must be positive"
  if n == 0:
    return 0
  while n > 0:
    #barray = n%2 + barray[:]
    barray.append(n%2)
    n = n >> 1
  barray.reverse()
  return barray

def modexp1(y, x, n):
  #convert x to a binary list
  x = binconvert(x)
   
  s = [1]
  r = x[:]
  for k in range (0, len(x)):
    if x[k] == 1:
      r[k] = (s[k] * y) % n
    else:
      r[k] = s[k]
    s.append ((r[k]**2)%n)
  return r[-1]

def modexp2(y, x, n):
  a = x
  b = 1
  c = y
  while a != 0:
    if a % 2 == 0:
      a = a/2
      c = (c**2) % n
    else:
      a = a -1
      b = (b * c) % n
  return b

# My implementation
def modexppow2(x,e,m):
	base = x
	while e > 1:
		base = (base * base) % m
		e >>= 1
	return base

def mymodexp(x,e,m):
	tot = 1
	pow1 = 1
	while e > 0:
		if e % 2 == 1:	
			tot *= modexppow2(x, pow1, m)
		pow1 <<= 1
		e >>= 1

	return tot % m

x = 55
e = 1171
m = 111233

if(len(sys.argv) > 1):
	x = int(sys.argv[1])

if(len(sys.argv) > 2):
	e = int(sys.argv[2])

if(len(sys.argv) > 3):
	m = int(sys.argv[3])

print("###### My FME ######")
start = time.time()
f = mymodexp(x,e,m)
print(time.time()-start)

"""print("###### Naive FME ######")
start = time.time()
a= naivefme(x,e,m)
print(time.time()-start)"""

print("###### FME1 (UMN) ######")
start = time.time()
b=fme1(x,e,m)
print(time.time()-start)

print("###### FME2 (Websters Progidy) ######")
start = time.time()
c=modexp1(x,e,m)
print(time.time()-start)

print("###### FME3 (Websters Progidy 2) ######")
start = time.time()
d=modexp2(x,e,m)
print(time.time()-start)

print("###### Built in FME ######")
start = time.time()
e = pow(x,e,m)
print(time.time()-start)

#print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
