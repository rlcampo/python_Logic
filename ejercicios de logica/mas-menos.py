arr = [1, 2, 3, -5, 7, 0]
a = len(arr)
a = int(a)
neg = 0
posi = 0
cero = 0
print(arr)
for n in arr:
    if n > 0:
        neg = 1 + neg
    elif n < 0:
        posi = 1 + posi
    elif n == 0:
        cero = 1 + cero
    # print(neg)    
    # print(posi)    
    # print(cero)    
    
    
m = neg / a
l = posi / a    
c = cero / a      
#print(m)
print("{0:.6f}".format(m))
print("{0:.6f}".format(l))
print("{0:.6f}".format(c))
#print(l)
#print(c)