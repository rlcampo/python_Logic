string = ["ab","ab","abc"]
queries = ["ab","abc","bc"]
results = []
l = 0

def matchingStrings(strings, queries):
#first few lines satisfies the constraints
    if len(strings) >= 1 and len(strings)<= 1000:
        if len(queries)>= 1 and len(strings)<= 1000:
            count_arr = {} # creating a dict to save each query count
            for query in queries:
                if len(query)>= 1 and len(query)<= 20:
                    count_arr[query] = 0
                    for string in strings:
                        if len(string)>= 1 and len(string)<= 20:
                            if query  == string.strip():
                                count_arr[query] = count_arr[query] + 1 #Esta es parecida a mi solución pero mas completa y aun asi no resolvia el 100% de los casos.
                                
    return list(count_arr.values())

def matchingStrings(strings, queries):
    # Write your code here
    output = []
    for i in range(len(queries)):
        output.append(strings.count(queries[i]))

    return output #esta funcion es sumamente mas eficiente. No la hice yo pero me resolvió muchas dudas