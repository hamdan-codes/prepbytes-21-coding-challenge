t = int(input())
for _ in range(t):
    n,k = input().split()
    n = int(n)
    q = int(input())
    c = 0
    found = []
    found.append(-1)
    for i in range(n):
        if k[i] == 'p':
            c += 1
            found.append(i)
    for i in range(q):
        x = int(input())
        if x <=c:
            print(found[x]+1)
        else:
            print(-1)
            
    
    
    
    
    
    
