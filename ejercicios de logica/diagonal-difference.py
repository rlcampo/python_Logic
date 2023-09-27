arr = [[11, 2, 4], 
       [4, 5, 6], 
       [10, 8, -12]]
s = 0
j = 0
s1 = 0
s2 = 0
Mlen = len(arr)
for i in range(Mlen):
    s = arr[i][i]
    j = arr[i][-1-i]
    s1 += int(s)
    s2 += int(j)
    #print(arr[i][i-1])
    #print(s1)
    #print(s2)
diff = abs(s1 - s2)
print(diff)
#print(range(Mlen))