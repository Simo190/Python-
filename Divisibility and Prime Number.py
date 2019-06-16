# Insert a number and check for its divisibility and if it is a Prime Number
# This script work perfectly until the multiple number of 107..

# For multiple number major of 107 this script work fine but not at the best!


# it's be better!


ppn = 'Your number could be a Prime Number'
fpn = 'Your number is divisibile for a Prime Number btw 67 and 107'
pn = 'Your number is a Prime Number!'
si = 'Your number is divisible for '
prime_number = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
intero = [67.0, 71.0, 73.0, 79.0, 83.0, 89.0, 97.0, 101.0, 103.0, 107.0]
print ('Type an integer number')
x = int (input ())
print ('Your number is ',x)
if x in prime_number: print (pn)
if x in intero: print (pn)

a = (x%2)
if a == 0: print (si, '2')

b = (x%3)
if b == 0: print (si, '3')

c = (x%5)
if c == 0: print (si, '5')

d = (x%7)
if d == 0: print (si, '7')

e = (x%11)
if e == 0: print (si, '11')

g = (x%13)
if g == 0: print (si, '13')

h = (x%17)
if h == 0: print (si, '17')

i = (x%19)
if i == 0: print (si ,'19')

l = (x%23)
if l == 0: print (si, '23')

m = (x%29)
if m == 0: print (si, '29')

n = (x%31)
if n == 0: print (si, '31')

o = (x%37)
if o == 0: print (si, '37')

p = (x%41)
if p == 0: print (si, '41')

q = (x%43)
if q == 0: print (si, '43')

r = (x%47)
if r == 0: print (si, '47')

s = (x%53)
if s == 0: print (si, '53')

t = (x%59)
if t == 0: print (si, '59')

u = (x%61)
if u == 0: print (si, '61')



if x > 3721:
   k = (x/intero[0])
   if k in intero : print (fpn)
   
if x > 3721:
   k = (x/intero[1])
   if k in intero : print (fpn)
   
if x > 3721:
   k = (x/intero[2])
   if k in intero : print (fpn)
   
   
if x > 3721:
   k = (x/intero[3])
   if k in intero : print (fpn)
   
   
if x > 3721:
   k = (x/intero[4])
   if k in intero : print (fpn)
   
   
if x > 3721:
   k = (x/intero[5])
   if k in intero : print (fpn)
   
if x > 3721:
   k = (x/intero[6])
   if k in intero : print (fpn)
   
if x > 3721:
   k = (x/intero[7])
   if k in intero : print (fpn)
   
if x > 3721:
   k = (x/intero[8])
   if k in intero : print (fpn)

if x > 3721:
   k = (x/intero[9])
   if k in intero : print (fpn)


if x not in intero:
   if x not in prime_number:
	  if x > 61:
		 if x < 11449:
			if a and b and c and d and e and g and h and i and l and m and n and o and p and q and r and s and t and u != 0: print (pn)

if x > 11449:
   if a and b and c and d and e and g and h and i and l and m and n and o and p and q and r and s and t and u != 0: print (ppn)

if x > 11449: 
   if a or b or c or d or e or g or h or i or l or m or n or o or p or q or r or s or t or u == 0: print ('WARNING\nYou have entered a number of which we can check the divisibility until to 107')
