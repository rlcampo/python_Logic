arr = [1, 2, 3, 4, 5]
resultado = 0
smin = 0
smax = 0
max = arr[0]
min = arr[0]   

for n in arr:
    if n > max:
        max = n
#print(max)

for n in arr:
    if n < min:
        min = n
#print(min)

for n in arr:
    resultado = n + resultado
    
smax = resultado - min
smin = resultado - max

print(smin, smax)