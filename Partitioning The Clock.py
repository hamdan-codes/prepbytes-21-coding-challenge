def getMaxLength(arr, n): 
    count = 0 
    result = 0 
    for i in range(0, 2*n): 
        if (arr[i%n] == 0): 
            count = 0
        else: 
            count+= 1 
            result = max(result, count)  

    return result
n = int(input())
a = [int(x) for x in input().split()]
print(getMaxLength(a,n))
