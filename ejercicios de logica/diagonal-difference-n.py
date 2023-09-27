arr = [[11, 2, 4], 
       [4, 5, 6], 
       [10, 8, -12]]
s = 0
j = 0
s1 = 0
s2 = 0
n = len(arr)
for i in range(n):
    s = arr[i][i]
    j = arr[i][-1-i]
    s1 += int(s)
    s2 += int(j)
diff = abs(s1 - s2)
print(diff)
#return diff
#print(range(Mlen))

#Codigo hecho por  Chat gpt
def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - i - 1]

    return abs(primary_sum - secondary_sum)