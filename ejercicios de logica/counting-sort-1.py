# def countingSort(arr):
#     output = []
#     for i in range(len(arr)):
#         output.append(arr.count(i))
#     return output

# arr = [1, 1, 3, 2, 1]
# output = []
# for i in range(len(arr)):
#     output.append(arr.count(i))
# print(output)

# def countingSort(arr):
#     output = []
#     index = {}
#     for i in enumerate(arr):
#         for num in i:
#             if num not in index:
#                 index[num] = [i]
#             else:
#                 index[num].append(i)
#     results = index[i]
#     for i in results:
#         output.append(results.count(i))
#     return output

# def countingSort(arr):
#     count_arr = {}
#     for ar in range(len(arr)):
#         count_arr[ar] = 0
#         for i in arr:
#             if ar not in count_arr:
#                 count_arr[i] = [arr]
#             else:
#                 count_arr[ar] = count_arr[ar] + 1
#     return list(count_arr.values())

# def countingsort(arr):
#     count_arr = {}
#     for ar in range(len(arr)):
#         count_arr[ar] = 0
#         count_arr.append(arr.count(ar))
#     return list(count_arr.values())

# arr = [1, 1, 3, 2, 1]
# output = []
# count_arr = {}
# for i, n in enumerate(arr):
#     count_arr[i] = 0
#     for num in n:
#         if num not in count_arr:
#             count_arr[num] = [i]
#         else:
#             count_arr[num].append(i)
#     print(count_arr)

N = int(input())

arr = list(map(int, input().split()))

freq = [0]*100

for i in arr:
    freq[i] = freq[i]+1


print (' '.join(map(str, freq)))